from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired. Length, Email, EqualTo

@app.route('/filter', methods=('GET', 'POST'))
def filter():
    if request.method == "POST":
        category = request.form['category']
        address = request.form['address']
        price = request.form['price']

        if not category:
            flash('Category is required!')
        elif not address:
            flash('Address is required!')
        elif not price:
            flash('Price is required!')
        else:
            messages.append({'category': category, 'address': address, 'price': price})
            return redirect(url_for('index'))

    return render_template('index.html')



