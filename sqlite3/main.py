import sqlite3
db = sqlite3.connect("books-collection.db")

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# Step 1: Set up the Flask app
app = Flask(__name__)

# Step 2: Configure the SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Step 3: Define the base class and initialize SQLAlchemy
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Step 4: Define the model (table)
class Book(db.Model):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

# Step 5: Create the table and insert data
with app.app_context():
    db.create_all()  # Create the schema (table)

    # Check if Harry Potter already exists to avoid duplicates
    if not db.session.query(Book).filter_by(title="Harry Potter").first():
        new_book = Book(
            id=1,
            title="Harry Potter",
            author="J. K. Rowling",
            rating=9.3
        )
        db.session.add(new_book)
        db.session.commit()
        print("✅ Book added to the database.")
    else:
        print("⚠️ Book already exists.")
