import csv
import sys

from tourist_app import app, db
from tourist_app.domain.restaurant import Restaurant
from tourist_app.domain.user_preferences import UserPreferences


def prepare_listing_user_pref(row):
    return UserPreferences(**row)


def load_user_preference_data():
    with open('user_prefereces.csv', newline='') as csv_file:
        csvreader = csv.DictReader(csv_file, quotechar='"')

        listings = [prepare_listing_user_pref(row) for row in csvreader]

        with app.app_context():
            db.session.add_all(listings)
            db.session.commit()


def prepare_listing(row):
    if row["delivery"] == "":
        row["delivery"] = 0.0
    if row["takeaway"] == "":
        row["takeaway"] = 0.0
    if row["dining_rating"] == "":
        row["dining_rating"] = 3.7
    if row["votes"] == "":
        row["votes"] = 3

    row["longitude"] = float(row["longitude"])
    row["latitude"] = float(row["latitude"])
    row["delivery"] = float(row["delivery"])
    row["takeaway"] = float(row["takeaway"])
    row["dining_rating"] = float(row["dining_rating"])
    row["votes"] = float(row["votes"])

    restaurant = Restaurant(**row)
    return restaurant


def load_restaurant_data():
    with open('fullRestaurants.csv', encoding="utf-8", newline='') as csv_file:
        csvreader = csv.DictReader(csv_file, quotechar='"')

        listings = [prepare_listing(row) for row in csvreader]

        with app.app_context():
            db.session.add_all(listings)
            db.session.commit()


def create_db_tables():
    with app.app_context():
        db.create_all()


def drop_all_tables():
    with app.app_context():
        db.drop_all()
        db.session.commit()

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("Nothing to run")
    arg = args[0]

    if arg == "run":
        app.run()
    elif arg == "setup":
        create_db_tables()
        # load_restaurant_data()
        # load_user_preference_data()
    elif arg == "drop-all":
        drop_all_tables()
    else:
        print("unknown command")


if __name__ == "__main__":
    main()
