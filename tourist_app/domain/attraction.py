from tourist_app import db, app

class Attraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(50))
    city = db.Column(db.String(50))
    description = db.Column(db.String(500))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    price = db.Column(db.Float)
    state = db.Column(db.String(50))
    street = db.Column(db.String(50))
    title = db.Column(db.String(50))
    totalScore = db.Column(db.Float)
    categories = db.Column(db.String(50))
    image_url = db.Column(db.String(500))

    def to_json(self):
        return {
            "property_name": self.title,
            "dining_rating": self.totalScore,
        }
