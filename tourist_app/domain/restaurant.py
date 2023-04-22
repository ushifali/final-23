from tourist_app import db, app

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurant_name = db.Column(db.String(50))
    cuisines = db.Column(db.String(100))
    pricing_for_2 = db.Column(db.Integer)
    locality = db.Column(db.String(100))
    dining_rating = db.Column(db.Float)
    website = db.Column(db.String(100))
    address = db.Column(db.String(100))
    phone_no = db.Column(db.Integer)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    timings = db.Column(db.String(50))
    highlights = db.Column(db.String(500))
    votes = db.Column(db.Float)
    delivery = db.Column(db.Float)
    takeaway = db.Column(db.Float)

    def to_json(self):
        return {
            "restaurant_name": self.restaurant_name,
            "dining_rating": self.dining_rating,
            "pricing_for_2": self.pricing_for_2

        }
