import csv

from tourist_app import app, db
from tourist_app.domain.restaurant import Restaurant
from tourist_app.domain.user_preferences import UserPreferences


# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()

if __name__ == '__main__':
    app.run()

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



# def prepare_listing_user_pref(row):
#     # row.pop("highlights")
#     # row["longitude"] = float(row["longitude"])
#     # row["longitude"] = float(row["longitude"])
#     print(row)
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