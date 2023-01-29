from words_app import app
from helpers.date_and_time import get_date, get_time
from words_app.models import User, Word
from flask import render_template


# quick route to show users database
@app.route("/show_users")
def show_users():
    date = get_date()
    user1 = User.query.all()
    return render_template("show_users.html", users = user1, date=date)

# quick route to show all words in database
@app.route("/all_words")
def all_words():
    words = Word.query.all()
    return render_template("/all_words.html", words = words)
