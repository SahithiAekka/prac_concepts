from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

all_books = []

def get_cover_url(title):
    # Query Open Library Search API for the book title
    query_url = f"https://openlibrary.org/search.json?title={title}"
    try:
        response = requests.get(query_url)
        data = response.json()
        if data['docs']:
            first_book = data['docs'][0]
            cover_id = first_book.get('cover_i')
            if cover_id:
                # Return Open Library cover URL
                return f"https://covers.openlibrary.org/b/id/{cover_id}-M.jpg"
    except Exception as e:
        print("Error fetching cover:", e)
    # Fallback placeholder image
    return "https://via.placeholder.com/100x150?text=No+Cover"

@app.route('/')
def home():
    return render_template('index.html', books=all_books)

@app.route('/add', methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        rating = request.form.get("rating")

        cover_url = get_cover_url(title)

        new_book = {
            "title": title,
            "author": author,
            "rating": rating,
            "cover_url": cover_url
        }
        all_books.append(new_book)
        return redirect('/')
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)
