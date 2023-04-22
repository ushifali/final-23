from tourist_app import db, app

class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    area = db.Column(db.String(50))
    city = db.Column(db.String(50))
    hotel_description = db.Column(db.String(500))
    hotel_facilities = db.Column(db.String(500))
    hotel_star_rating = db.Column(db.Float)
    image_urls = db.Column(db.String(500))
    locality = db.Column(db.String(50))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    pageurl = db.Column(db.String(100))
    property_type = db.Column(db.String(20))
    province = db.Column(db.String(50))
    room_count = db.Column(db.Float)
    room_facilities = db.Column(db.String(100))
    room_type = db.Column(db.String(50))
    state = db.Column(db.String(50))
    rating = db.Column(db.Float)
    
    def to_json(self):
        return {
            "property_name": self.property_name,
            "dining_rating": self.rating,
            "hotel_star_rating": self.hotel_star_rating
        }