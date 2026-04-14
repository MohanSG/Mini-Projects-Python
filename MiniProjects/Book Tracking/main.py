from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, select

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Name: Mapped[str]
    Author: Mapped[str]
    Rating: Mapped[int]
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
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    all_books = Book.query.all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        data = request.form

        book = Book(
            Name = data['bookName'],
            Author = data['bookAuthor'],
            Rating = data['bookRating']
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    elif request.method == "GET":
        return render_template('add.html')

@app.route("/edit/<int:book_id>", methods=['GET', 'POST'])
def edit(book_id):
    book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    if request.method == "GET":
        print(book.id)
        return render_template('edit.html', book=book)
    elif request.method == "POST":
        print("posting")
        data = request.form
        print(f"The new rating is {data['newRating']}")
        book.Rating = data['newRating']
        db.session.commit()
        return redirect(url_for('home'))

@app.route("/delete/<int:book_id>")
def delete(book_id):
    with app.app_context():
        book = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

