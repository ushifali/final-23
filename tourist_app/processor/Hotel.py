from tourist_app.Contract.hotels import ContractHotel
from tourist_app.Contract.user_preferences import ContractUserPreferences

from tourist_app.domain.hotel import Hotel
from math import radians, cos, sin, asin, sqrt

from tourist_app.domain.user import User
from tourist_app.domain.user_preferences import UserPreferences

import numpy as np

def find_hotels(latitude, longitude, user_id, distance, price, rating):
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

    all_hotels = Hotel.query.all()
    recommendations = get_recommendations(all_hotels, latitude, longitude, distance, price, rating)
    contract_hotels = map_to_contract_hotel(recommendations)

    final_recommended_hotels = recommend_hotels(contract_user_preferences[user_id], contract_hotels)

    return final_recommended_hotels[:10]


def map_to_contract_hotel(recommendations):
    contractHotels = []
    for recommendation in recommendations:
        recommendation[0].hotel_facilities = recommendation[0].hotel_facilities.split("|")
        contractHotels.append(ContractHotel(id=recommendation[0].id,
                                                      property_name=recommendation[0].property_name,
                                                      address=recommendation[0].address,
                                                      city=recommendation[0].city,
                                                      hotel_description=recommendation[0].hotel_description,
                                                      hotel_facilities=recommendation[0].hotel_facilities,
                                                      hotel_star_rating=recommendation[0].hotel_star_rating,
                                                      locality=recommendation[0].locality,
                                                      room_type=recommendation[0].room_type,
                                                      state=recommendation[0].state,
                                                      rating=recommendation[0].rating,                                                      
                                                      latitude=recommendation[0].latitude,
                                                      longitude=recommendation[0].longitude,
                                                      distance=recommendation[1]))
    return contractHotels


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


def get_recommendations(hotels, user_latitude, user_longitude, max_distance=2000, max_price=1200,
                        min_dining_rating=3.5, n_recommendations=100):
    # Calculate distance from user's location to each restaurant
    distances = []
    for restaurant in hotels:
        distance = haversine_distance(user_latitude, user_longitude, restaurant.latitude, restaurant.longitude)
        if distance <= max_distance and restaurant.hotel_star_rating >= min_dining_rating:
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
    '''
    cuisine_array1 = np.array(cuisine_list1)
    cuisine_array2 = np.array(cuisine_list2)
    dot_product = np.dot(cuisine_array1, cuisine_array2)
    magnitude1 = np.linalg.norm(cuisine_array1)
    magnitude2 = np.linalg.norm(cuisine_array2)
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    else:
        return dot_product / (magnitude1 * magnitude2)
    '''


# define a function to recommend restaurants based on user preferences and restaurant cuisines
def recommend_hotels(user_preferences, hotel_list):
    recommended_hotels = []
    for restaurant in hotel_list:
        cosine_sim = cosine_similarity(user_preferences.facilities, restaurant.hotel_facilities)
        if cosine_sim > 0:
            recommended_hotels.append(restaurant)
    return recommended_hotels
