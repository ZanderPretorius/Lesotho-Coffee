from tkinter import Label
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from h11 import Data
from numpy import average
from wtforms import StringField, SubmitField, FloatField, Label, BooleanField
from wtforms.validators import DataRequired, URL
import requests
from country_flag import FlagFetch
import json



app = Flask(__name__)
app.config["SECRET_KEY"] = "fbhsikufgkbwigfuidekd7i6i"
Bootstrap(app)


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes-DB.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=False, nullable=False)
    city = db.Column(db.String(250), nullable=False)
    country = db.Column(db.String(250), nullable=False)
    google_maps_url = db.Column(db.String(1150), unique=True, nullable=False)
    image_link = db.Column(db.String(1150), unique=True, nullable=False)
    has_pets = db.Column(db.Boolean, default=False)
    has_alcohol = db.Column(db.Boolean, default=False)
    has_calls = db.Column(db.Boolean, default=False)
    has_mask = db.Column(db.Boolean, default=False)
    has_food = db.Column(db.Boolean, default=False)
    has_wifi = db.Column(db.Boolean, default=False)
    has_toilet = db.Column(db.Boolean, default=False)
    has_power = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Cafe {self.name}>'


class CreateCafe(FlaskForm):
    name = StringField("Cafe Name", validators=[DataRequired()])
    country = StringField("Country", validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired()])
    google_maps_url = StringField(
        "Google Maps URL", validators=[DataRequired()])
    image_link = StringField("Image Link: ")
    has_pets = BooleanField('Are Pets Allowed?')
    has_alcohol = BooleanField('Is alcohol served?')
    has_calls = BooleanField('May You Take Calls?')
    has_mask = BooleanField('Are Masks Required?')
    has_food = BooleanField('Is Food Offered?')
    has_wifi = BooleanField('Is Free Wifi Acess Available')
    has_toilet = BooleanField('Are there Bathrooms nearby?')
    has_power = BooleanField('Is Electricity Access Available')
    submit = SubmitField("Add Item")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/view-cafes")
def view_cafes():
    db_all_cafes = db.session.query(Cafe).all()
    # print(db_all_cafes)
    return render_template("all_cafes.html", all_cafes=db_all_cafes)


@app.route('/view-cafe-by-id-<int:cafe_id>')
def view_cafe_by_id(cafe_id):

    requested_cafe = Cafe.query.get(cafe_id)

    return render_template('view-cafe.html', cafe = requested_cafe)

@app.route('/country-<country_name>')
def get_country_data(country_name):
    country_name = (country_name)
    fetch = FlagFetch(country_name)
    cca3 = fetch.get_cca3()
    flag = fetch.get_flag_png()
    name = fetch.get_name()
    return (f"{cca3} <img src={flag}>  {name}")


@app.route("/add-cafe", methods=["GET", "POST"])
def add():
    form = CreateCafe()
    if form.validate_on_submit():
        added_cafe = Cafe(
            name=form.name.data,
            city=form.city.data,
            country=form.country.data,
            google_maps_url=form.google_maps_url.data,
            image_link=form.image_link.data,
            has_alcohol=form.has_alcohol.data,
            has_calls=form.has_calls.data,
            has_pets=form.has_pets.data,
            has_power=form.has_power.data,
            has_toilet=form.has_toilet.data,
            has_wifi=form.has_wifi.data,
            has_mask=form.has_mask.data,
            has_food=form.has_food.data
        )
        db.session.add(added_cafe)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route("/delete-cafe-<int:cafe_id>")
def delete_cafe(cafe_id):

    cafe_to_delete = Cafe.query.get(cafe_id)
    db.session.delete(cafe_to_delete)
    db.session.commit()
    return(redirect(url_for('view_cafes')))


# THIS IS AN EDIT MOOOOOOO! 

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True)
