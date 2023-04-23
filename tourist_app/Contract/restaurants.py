from tourist_app.domain.restaurant import Restaurant


class ContractRestaurant():
    def __init__(self, id, restaurant_name, cuisines, pricing_for_2, dining_rating, address, locality, phone_no,
                 latitude, longitude, timings, distance):
        self.id = id
        self.restaurant_name = restaurant_name
        self.cuisines = cuisines
        self.pricing_for_2 = pricing_for_2
        self.dining_rating = dining_rating
        self.address = address
        self.locality = locality
        self.phone_no = phone_no
        self.latitude = latitude
        self.longitude = longitude
        self.timings = timings
        self.distance = distance

    def to_json(self):
        return {
            "restaurant_name": self.restaurant_name,
            "dining_rating": self.dining_rating,
            "pricing_for_2": self.pricing_for_2,
            "distance": self.distance,
            "timings": self.timings,
            "address": self.address
        }

def map_to_contract_restaurant(restaurant: Restaurant, distance):
    return ContractRestaurant(restaurant.id,
                              restaurant.restaurant_name,
                              restaurant.cuisines,
                              restaurant.pricing_for_2,
                              restaurant.dining_rating,
                              restaurant.address,
                              restaurant.locality,
                              restaurant.phone_no,
                              restaurant.latitude,
                              restaurant.longitude,
                              restaurant.timings,
                              distance)


