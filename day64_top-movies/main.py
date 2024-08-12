from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

import requests

MOVIE_DB_URL = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"
HEADERS = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjMTU1NWEzYWQ4YmMwZDdjODJlOGYxMzNkYjEyODE3MCIsInN1YiI6IjY1YWVmYzJhMzk3NTYxMDEwYzQ1ZGIxYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ZjKzjTQU_A8AesNr4RxYiaaE34u_633tt5tUMwGP_nU"
}
MOVIE_DB_SELECT_URL = "https://api.themoviedb.org/3/movie/"

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-movies-collection.db"
# initialize the app with the extension
db.init_app(app)


##CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[str] = mapped_column(String(250), nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[float] = mapped_column(Float, nullable=False)
    review: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()


#STORE DATA RECEIVED FROM DATABASE
all_movies = []


@app.route("/")
def home():
    #READ ALL RECORDs
    result = db.session.execute(db.select(Movie).order_by(Movie.title))
    all_movies = result.scalars()
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == "POST":
        movie_title = request.form.get("movie_title")
        response = requests.get(MOVIE_DB_URL, headers=HEADERS, params={"query": movie_title})
        options = response.json()["results"]
        return render_template('select.html', options=options)
    return render_template('add.html')


@app.route("/select/<int:id>")
def select(id):
    response = requests.get(MOVIE_DB_SELECT_URL, params={"movie_id": id})
    print(response)
    return redirect(url_for('home'))


@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    movie = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
    if request.method == 'POST':
        #UPDATE A RECORD
        book_to_update = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
        book_to_update.rating = request.form.get('movie_rating')
        book_to_update.review = request.form.get('movie_review')
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie)


@app.route("/delete/<int:id>")
def delete(id):
    #DELETE A RECORD COMPLETELY
    book_to_delete = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
