from tourist_app.Contract.attractions import ContractAttraction
from tourist_app.Contract.user_preferences import ContractUserPreferences

from tourist_app.domain.attraction import Attraction
from math import radians, cos, sin, asin, sqrt

from tourist_app.domain.user import User
from tourist_app.domain.user_preferences import UserPreferences

import numpy as np

def find_attractions(latitude, longitude, user_id, distance, price, rating):
    user_preferences = UserPreferences.query.all()

    contract_user_preferences = []
    for user_preference in user_preferences:
        cuisines = user_preference.cuisines.split(",")
        categories = user_preference.categories.split(",")
        facilities = user_preference.facilities.split(",")
        contract_user_preferences.append(ContractUserPreferences(user_id=user_preference.user_id,
                                                                 categories=categories,
                                                                 max_price=user_preference.max_price,
                                                                 locations=user_preference.locations,
                                                                 min_rating=user_preference.min_rating,
                                                                 cuisines=cuisines,
                                                                 max_distance=user_preference.max_distance,
                                                                 facilities=facilities
                                                                 ))

    distance = float(distance)
    price = float(price)
    rating = float(rating)

    all_attractions = Attraction.query.all()
    recommendations = get_recommendations(all_attractions, latitude, longitude, distance, price, rating)
    contract_attractions = map_to_contract_attraction(recommendations)

    final_recommended_attractions = recommend_attractions(contract_user_preferences[user_id], contract_attractions)

    return final_recommended_attractions[:10]


def map_to_contract_attraction(recommendations):
    contractAttractions = []
    for recommendation in recommendations:
        recommendation[0].categories = recommendation[0].categories.split(",")
        contractAttractions.append(ContractAttraction(id=recommendation[0].id, 
                                                    title=recommendation[0].title, 
                                                    address=recommendation[0].address, 
                                                    city=recommendation[0].city, 
                                                    description=recommendation[0].description, 
                                                    street=recommendation[0].street, 
                                                    totalScore=recommendation[0].totalScore, 
                                                    categories=recommendation[0].categories, 
                                                    latitude=recommendation[0].latitude, 
                                                    longitude=recommendation[0].longitude, 
                                                    distance=recommendation[1]))
    return contractAttractions


def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r


def get_recommendations(attractions, user_latitude, user_longitude, max_distance=2000, max_price=1200,
                        min_dining_rating=3.5, n_recommendations=100):
    # Calculate distance from user's location to each restaurant
    distances = []
    for restaurant in attractions:
        if restaurant.totalScore:
            distance = haversine_distance(user_latitude, user_longitude, restaurant.latitude, restaurant.longitude)
            if distance <= max_distance and float(restaurant.totalScore) >= min_dining_rating:
                distances.append((restaurant, distance))

    # Sort restaurants by distance and return top n recommendations
    distances.sort(key=lambda x: x[1])
    recommendations = [(r, d) for r, d in distances][:n_recommendations]
    return recommendations


def cosine_similarity(cuisine_list1, cuisine_list2):
    common_cuisines = set(cuisine_list1).intersection(set(cuisine_list2))
    # print(common_cuisines)
    magnitude1 = len(cuisine_list1)
    magnitude2 = len(cuisine_list2)
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    else:
        return len(common_cuisines) / (magnitude1 * magnitude2) ** 0.5
    


# define a function to recommend restaurants based on user preferences and restaurant cuisines
def recommend_attractions(user_preferences, attraction_list):
    recommended_attractions = []
    for restaurant in attraction_list:
        cosine_sim = cosine_similarity(user_preferences.categories, restaurant.categories)
        if cosine_sim > 0:
            recommended_attractions.append(restaurant)
    return recommended_attractions
