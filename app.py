import csv

from tourist_app import app, db
from tourist_app.domain.restaurant import Restaurant
from tourist_app.domain.user_preferences import UserPreferences

#
# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#
if __name__ == '__main__':
    app.run()

# def prepare_listing(row):
#     if row["delivery"] == "":
#         row["delivery"] = 0.0
#     if row["takeaway"] == "":
#         row["takeaway"] = 0.0
#     if row["dining_rating"] == "":
#         row["dining_rating"] = 3.7
#     if row["votes"] == "":
#         row["votes"] = 3
#
#     row["longitude"] = float(row["longitude"])
#     row["latitude"] = float(row["latitude"])
#     row["delivery"] = float(row["delivery"])
#     row["takeaway"] = float(row["takeaway"])
#     row["dining_rating"] = float(row["dining_rating"])
#     row["votes"] = float(row["votes"])
#
#     restaurant = Restaurant(**row)
#     # print(restaurant.id)
#     # print(restaurant.id)
#     return restaurant
#
#
# if __name__ == '__main__':
#     with open('fullRestaurants.csv', encoding="utf-8", newline='') as csv_file:
#         csvreader = csv.DictReader(csv_file, quotechar='"')
#         # for row in csvreader:
#         #     print(row)
#         #     print(Restaurant(**row))
#         # #
#         listings = [prepare_listing(row) for row in csvreader]
#         # print("woooooo")
#         #
#         with app.app_context():
#             db.session.add_all(listings)
#             db.session.commit()

# def prepare_listing_user_pref(row):
#     # row.pop("highlights")
#     # row["longitude"] = float(row["longitude"])
#     # row["longitude"] = float(row["longitude"])
#     # print(row)
#     return UserPreferences(**row)
#
#
# if __name__ == '__main__':
#     with open('user_prefereces.csv', newline='') as csv_file:
#         csvreader = csv.DictReader(csv_file, quotechar='"')
#         # for row in csvreader:
#         #     print(row)
#         #     print(Restaurant(**row))
#         # #
#         listings = [prepare_listing_user_pref(row) for row in csvreader]
#         # print("woooooo")
#         #
#         with app.app_context():
#             db.session.add_all(listings)
#             db.session.commit()

# if __name__ == '__main__':
#     with app.app_context():
#         db.drop_all()

# if __name__=='__main__':
#     with app.app_context():
#         i=Restaurant.__table__.drop(db.engine)
#         print(i)
#         db.session.commit()
#
# if __name__=='__main__':
#     with app.app_context():
#         print(len(Restaurant.query.all()))

# def prepare_listing(row):
#     row.pop("highlights")
#     row["longitude"] = float(row["longitude"])
#     row["longitude"] = float(row["longitude"])
#     return Restaurant(**row)
#
#
# if __name__ == '__main__':
#     with open('restaurant.csv', newline='') as csv_file:
#         csvreader = csv.DictReader(csv_file, quotechar='"')
#         # for row in csvreader:
#         #     print(row)
#         #     print(Restaurant(**row))
#         # #
#         listings = [prepare_listing(row) for row in csvreader]
#         # print("woooooo")
#
#         with app.app_context():
#             db.session.add_all(listings)
#             db.session.commit()
