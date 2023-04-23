from flask import redirect, url_for, render_template, flash, request, session, jsonify
from flask_login import logout_user, login_user, current_user, login_required

from tourist_app import app, db, bcrypt
from tourist_app.domain.user import User
from tourist_app.domain.restaurant import Restaurant
from tourist_app.domain.attraction import Attraction
from tourist_app.domain.hotel import Hotel
from tourist_app.forms import LoginForm, RegistrationForm
from tourist_app.processor.Restaurant import find_restaurants
from tourist_app.processor.Hotel import find_hotels
from tourist_app.processor.Attraction import find_attractions


# @app.route('/')
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


@app.route("/index", methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html',
                           cat=[{'cat': 'Attractions'}, {'cat': 'Restaurants'}, {'cat': 'Hotels'}],
                           prc=[{'prc': '100-500'}, {'prc': '500-1000'}, {'prc': '1000-3000'}, {'prc': '3000-more'}],
                           )

@app.route('/')
@app.route("/category")
def category():
    restaurants = db.session.execute(db.select(Restaurant).filter_by(dining_rating=4.9))
    hotels = db.session.execute(db.select(Hotel).filter_by(city='Bangalore', rating=5.0))
    attractions = db.session.execute(db.select(Attraction).filter_by(city='Bengaluru', totalScore=5.0))

    return render_template('category.html', restaurants=restaurants, hotels=hotels, attractions=attractions)


@app.route('/get_location', methods=['POST'])
def get_location():
    latitude = request.json['latitude']
    longitude = request.json['longitude']

    session['latitude'] = latitude
    session['longitude'] = longitude
    return jsonify(success=True)


@app.route("/listing", methods=['GET', 'POST'])
@login_required
def listing():
    if request.method == "POST":
        category = request.form.get('category')
        distance = request.form.get('distance')
        price = request.form.get('price')
        rating = request.form.get('rating')

        # user_id = 7
        # latitude = 12.9716034  
        # longitude = 77.5946976
        user_id = session['user_id']
        latitude = session.get('latitude')
        longitude = session.get('longitude')

        print(latitude, longitude, user_id)

        form_data = [
            category, distance, price, rating
        ]
        
        if category == 'Restaurants':
            restaurants = find_restaurants(latitude, longitude, user_id, distance, price, rating)
            return render_template('listing.html', data=form_data, restaurants=restaurants)
        elif category == 'Hotels':
            hotels = find_hotels(latitude, longitude, user_id, distance, price, rating)
            return render_template('listing.html', data=form_data, hotels=hotels)
        elif category == 'Attractions':
            attractions = find_attractions(latitude, longitude, user_id, distance, price, rating)
            return render_template('listing.html', data=form_data, attractions=attractions)

    return render_template('listing.html')


@app.route("/contact")
def contact():
    latitude = session.get('latitude')
    longitude = session.get('longitude')

    return render_template('contact.html', latitude = latitude, longitude = longitude)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/", methods=['get', 'post'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        session['user_id'] = current_user.id
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            session['user_id'] = user.id
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
