from flask import Flask, render_template, request, url_for, flash, redirect
app = Flask(__name__)

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route("/", methods=['get', 'post'])
@app.route("/index", methods=['get', 'post'])
def index():
    if request.method == "post":
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
            return redirect(url_for('category'), messages=messages)
    return render_template('index.html', 
        cat=[{'cat': 'Attractions'}, {'cat': 'Restaurants'}, {'cat': 'Hotels'}],
        prc=[{'prc': '100-500'}, {'prc': '500-1000'}, {'prc': '1000-3000'}, {'prc': '3000-more'}],
        messages = messages
    )

@app.route("/category")
def category():
    return render_template('category.html')

@app.route("/listing")
def listing():
    return render_template('listing.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')



if __name__ == "__main__":
    app.run(debug=True)