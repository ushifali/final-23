from tourist_app import app, db
from tourist_app.processor.Restaurant import find_restaurants


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

@app.route("/restaurants/<float:latitude>/<float:longitude>/<int:user_id>")
def restaurants_list(latitude, longitude, user_id):
    restaurants = find_restaurants(latitude, longitude, user_id)
    response = []
    for restaurant in restaurants:
        response.append(restaurant.to_json())

    return response
