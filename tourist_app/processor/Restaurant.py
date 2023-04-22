from tourist_app.Contract.restaurants import ContractRestaurant
from tourist_app.Contract.user_preferences import ContractUserPreferences

from tourist_app.domain.restaurant import Restaurant
from math import radians, cos, sin, asin, sqrt

from tourist_app.domain.user import User
from tourist_app.domain.user_preferences import UserPreferences


def find_restaurants(latitude, longitude, user_id):
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

    all_restaurants = Restaurant.query.all()
    recommendations = get_recommendations(all_restaurants, latitude, longitude)
    contractRestaurants = []
    for recommendation in recommendations:
        cuisines = recommendation[0].cuisines.split(",")
        contractRestaurants.append(ContractRestaurant(id=recommendation[0].id,
                                                      restaurant_name=recommendation[0].restaurant_name,
                                                      cuisines=cuisines,
                                                      pricing_for_2=recommendation[0].pricing_for_2,
                                                      dining_rating=recommendation[0].dining_rating,
                                                      address=recommendation[0].address,
                                                      locality=recommendation[0].locality,
                                                      phone_no=recommendation[0].phone_no,
                                                      latitude=recommendation[0].latitude,
                                                      longitude=recommendation[0].longitude,
                                                      timings=recommendation[0].timings,
                                                      distance=recommendation[1]))

    final_recommended_restaurants = recommend_restaurants(contract_user_preferences[user_id], contractRestaurants)

    return final_recommended_restaurants


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


def get_recommendations(restaurants, user_latitude, user_longitude, max_distance=2000, max_price=1200,
                        min_dining_rating=3.5, n_recommendations=10):
    # Calculate distance from user's location to each restaurant
    distances = []
    for restaurant in restaurants:
        distance = haversine_distance(user_latitude, user_longitude, restaurant.latitude, restaurant.longitude)
        if distance <= max_distance and restaurant.pricing_for_2 <= max_price and restaurant.dining_rating >= min_dining_rating:
            distances.append((restaurant, distance))

    # Sort restaurants by distance and return top n recommendations
    distances.sort(key=lambda x: x[1])
    recommendations = [(r, d) for r, d in distances][:n_recommendations]
    return recommendations


def cosine_similarity(cuisine_list1, cuisine_list2):
    common_cuisines = set(cuisine_list1).intersection(set(cuisine_list2))
    print(common_cuisines)
    magnitude1 = len(cuisine_list1)
    magnitude2 = len(cuisine_list2)
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    else:
        return len(common_cuisines) / (magnitude1 * magnitude2) ** 0.5


# define a function to recommend restaurants based on user preferences and restaurant cuisines
def recommend_restaurants(user_preferences, restaurant_list):
    recommended_restaurants = []
    for restaurant in restaurant_list:
        print("Restaurant Name")
        print(restaurant.restaurant_name)
        print(user_preferences.cuisines)
        print(restaurant.cuisines)
        cosine_sim = cosine_similarity(user_preferences.cuisines, restaurant.cuisines)
        if cosine_sim > 0:
            recommended_restaurants.append(restaurant)
    return recommended_restaurants
