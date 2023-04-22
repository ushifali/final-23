from tourist_app import db


class UserPreferences(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    categories = db.Column(db.String(500))
    max_price = db.Column(db.Integer)
    locations = db.Column(db.String(500))
    min_rating = db.Column(db.Float)
    cuisines = db.Column(db.String(500))
    max_distance = db.Column(db.Float)
    facilities = db.Column(db.String(500))

    def to_json(self):
        return {
            "user_id": self.user_id,
            "categories": self.categories,
            "cuisines": self.cuisines,
            "facilities": self.facilities
        }
