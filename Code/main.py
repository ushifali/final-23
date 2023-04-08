from flask import Flask, render_template, url_for, flash, redirect

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

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