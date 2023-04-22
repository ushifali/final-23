class ContractUserPreferences():
    def __init__(self, user_id, categories, max_price, locations, min_rating, cuisines, max_distance, facilities):
        self.user_id = user_id
        self.categories = categories
        self.max_price = max_price
        self.locations = locations
        self.min_rating = min_rating
        self.cuisines = cuisines
        self.max_distance = max_distance
        self.facilities = facilities

    def to_json(self):
        return {
            "user_id": self.user_id,
            "categories": self.categories,
            "cuisines": self.cuisines,
            "facilities": self.facilities
        }
