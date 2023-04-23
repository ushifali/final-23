from tourist_app.domain.attraction import Attraction


class ContractAttraction():
    def __init__(self, id, title, address, city, description, street, totalScore, categories,
                 latitude, longitude, distance):
        self.id = id
        self.title = title
        self.address = address
        self.city = city
        self.description = description
        self.street = street
        self.totalScore = totalScore
        self.categories = categories
        self.latitude = latitude
        self.longitude = longitude
        self.distance = distance

    def to_json(self):
        return {
            "restaurant_name": self.title,
            "dining_rating": self.totalScore,
            "distance": self.distance,
            "address": self.address
        }

def map_to_contract_attraction(attraction: Attraction, distance):
    return ContractAttraction(attraction.id, 
                                attraction.title, 
                                attraction.address, 
                                attraction.city, 
                                attraction.description, 
                                attraction.street, 
                                attraction.totalScore, 
                                attraction.categories, 
                                attraction.latitude, 
                                attraction.longitude, 
                                distance)


