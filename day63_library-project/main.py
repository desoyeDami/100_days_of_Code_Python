from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

import sqlite3

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) "
#                "NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

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


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)


##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

#STORE DATA RECEIVED FROM DATABASE
all_books = []


@app.route('/')
def home():
    #READ ALL RECORDs
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        req = request.form
        # CREATE RECORD
        new_book = Book(
            title=req.get('bname'),
            author=req.get('author'),
            rating=req.get('rating')
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    book = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
    if request.method == 'POST':
        #UPDATE A RECORD
        book_to_update = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
        book_to_update.rating = request.form.get('book_rating')
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', book=book)


@app.route("/delete/<int:id>")
def delete(id):
    #DELETE A RECORD COMPLETELY
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
