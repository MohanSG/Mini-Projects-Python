import os

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(unique=True)
    year: Mapped[int]
    description: Mapped[str]
    rating: Mapped[int]
    ranking: Mapped[int]
    review: Mapped[str]
    img_url:Mapped[str]

class EditForm(FlaskForm):
    rating = IntegerField('rating', validators=[DataRequired()])
    review = StringField('review', validators=[DataRequired()])
    submit = SubmitField('submit')

class AddForm(FlaskForm):
    movie_title = StringField('Movie Title', name='title', validators=[DataRequired()])
    submit = SubmitField('submit')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
app.secret_key = "my_secret_key"
load_dotenv()


Bootstrap5(app)

# CREATE DB
db = SQLAlchemy(model_class=Base)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
db.init_app(app)

# CREATE TABLE
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie).order_by(Movie.rating.asc())).scalars().all()
    rank_count=len(movies)
    for movie in movies:
        movie.ranking = rank_count
        rank_count -= 1
    return render_template("index.html", movies=movies)

@app.route("/edit/<int:movie_id>", methods=['GET', 'POST'])
def edit(movie_id):
    form = EditForm()
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        print("posting edit form")

        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()

        return redirect(url_for('home'))

    return render_template("edit.html", form=form, movie=movie)

@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        results = film_search_results(form.movie_title.data)
        return render_template('select.html', results=results)

    return render_template('add.html', form=form)

@app.route("/select/<string:imdb_id>")
def search(imdb_id):
    film_detail = film_search(imdb_id)
    new_movie = Movie(
        title=film_detail['Title'],
        img_url=film_detail['Poster'],
        year=film_detail['Year'],
        description=film_detail['Plot'],
        rating=2,
        review="TBA",
        ranking=999
    )
    db.session.add(new_movie)
    db.session.commit()

    movie_entry = db.session.execute(db.select(Movie).where(Movie.title == film_detail['Title'])).scalar()
    return redirect(url_for('edit', movie_id=movie_entry.id, movie=movie_entry))

def film_search_results(film_title):
    url="http://www.omdbapi.com"
    params = {
        "apikey" : os.environ['OMDB_API'],
        "s" : film_title,
        "type": "movie",
        "r" : "json"
    }
    response = requests.get(url, params=params)
    return response.json()

def film_search(imdb_id):
    url="http://www.omdbapi.com"
    params = {
        "apikey" : os.environ['OMDB_API'],
        "i" : imdb_id,
        "type": "movie",
        "r" : "json"
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
