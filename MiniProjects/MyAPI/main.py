from flask import Flask, jsonify, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods=['GET'])
def random_cafe():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    print(cafes)
    cafe = random.choice(cafes)

    return jsonify(cafe.to_dict())

    # return jsonify(
    #     cafe = {
    #         "id" : cafe.id,
    #         "name" : cafe.name,
    #         "map_url" : cafe.map_url,
    #         "location" : cafe.location,
    #         "has_sockets" : cafe.has_sockets,
    #         "has_toilet" : cafe.has_toilet,
    #         "has_wifi" : cafe.has_wifi,
    #         "can_take_calls" : cafe.can_take_calls,
    #         "seats" : cafe.seats,
    #         "coffee_price" : cafe.coffee_price
    #     }
    # )

@app.route("/all", methods=['GET'])
def all():
    all_cafes = db.session.execute(db.select(Cafe)).scalars()
    cafes = [cafe.to_dict() for cafe in all_cafes]

    return jsonify(cafes)

@app.route("/search", methods=['GET'])
def search():
    loc = request.args.get('loc')
    loc_cafes = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars().all()

    if loc_cafes:
        cafes = [cafe.to_dict() for cafe in loc_cafes]
        return jsonify(cafes)
    else:
        return {
            "error" : {
                "Not found" : "Sorry, we don't have a cafe at that location"
            }
        }

@app.route("/add", methods=['GET', 'POST'])
def add():
    cafe = Cafe()

    try:
        cafe.name = request.args.get('name')
        cafe.seats = request.args.get('seats')
        cafe.img_url = request.args.get('img_url')
        cafe.map_url = request.args.get('map_url')
        cafe.location = request.args.get('location')
        cafe.can_take_calls = bool(request.args.get('can_take_calls'))
        cafe.coffee_price = request.args.get('coffee_price')
        cafe.has_sockets = bool(request.args.get('has_sockets'))
        cafe.has_toilet = bool(request.args.get('has_toilet'))
        cafe.has_wifi = bool(request.args.get('has_wifi'))

        db.session.add(cafe)
        db.session.commit()
    except TypeError:
        return {
            "response" : {
                "error" : "Wrong Type"
            }
        }
    else:
        return {
            "response" : {
                "success" : "Added successfully"
            }
    }

@app.route("/update-price/<cafe_id>", methods = ['PATCH'])
def update(cafe_id):
    try:
        cafe = Cafe.query.get(cafe_id)
        updated_price = request.args.get("updated_price")
        cafe.coffee_price = updated_price
        db.session.commit()
    except AttributeError:
        return {
            "response" : {
                "error" : "Something went wrong, check the ID again"
            }
        }
    else:
        return {
            "response" : {
                "success" : "success"
            }
        }

@app.route("/report-closed/<cafe_id>", methods = ['DELETE'])
def closed(cafe_id):
    key = "TopSecretKey"

    if request.args.get("api-key") == key:
        try:
            cafe = Cafe.query.get(cafe_id)
            db.session.delete(cafe)
            db.session.commit()

        except AttributeError:
            return {
                "response" : {
                    "Error" : "Something went wrong, please check the attributes"
                }
            }
        else:
            return {
                "response" : {
                    "Success" : "Cafe deleted successfully"
                }
            }
    else:
        return {
            "response" : {
                "Error" : "Invalid API Key"
            }
        }
# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
