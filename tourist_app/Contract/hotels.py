from tourist_app.domain.hotel import Hotel


class ContractHotel():
    def __init__(self, id, property_name, address, city, hotel_description, hotel_facilities, hotel_star_rating, locality,
                 room_type, state, rating, latitude, longitude, distance):
        self.id = id
        self.property_name = property_name
        self.address = address
        self.city = city
        self.hotel_description = hotel_description
        self.hotel_facilities = hotel_facilities
        self.hotel_star_rating = hotel_star_rating
        self.locality = locality
        self.room_type = room_type
        self.state = state
        self.rating = rating
        self.latitude = latitude
        self.longitude = longitude
        self.distance = distance

    def to_json(self):
        return {
            "restaurant_name": self.property_name,
            "dining_rating": self.rating,
            "distance": self.distance,
            "address": self.address
        }

def map_to_contract_hotel(hotel: Hotel, distance):
    return ContractHotel(hotel.id,
                        hotel.property_name,
                        hotel.address,
                        hotel.city,
                        hotel.hotel_description,
                        hotel.hotel_facilities,
                        hotel.hotel_star_rating,
                        hotel.locality,
                        hotel.room_type,
                        hotel.state,
                        hotel.rating,
                        hotel.latitude,
                        hotel.longitude,
                        distance)


