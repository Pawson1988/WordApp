from words_app import app, db
from words_app.models import Word
from flask import render_template, request, redirect, session, abort
from helpers.date_and_time import get_date, get_time


# First route to show words or login
@app.route("/")
def hello():
    return redirect("/show_words")

# Route to show words from database
@app.route("/show_words")
def show_words():
    words = Word.query.filter_by(user_id = session['id']).all()
    print(words)
    return render_template("show_words.html", words = words)

# form route to get words from index.html, save in dictionary and redirect to showdb
@app.route("/add_word", methods=["GET","POST"])
def add_word():

    if request.method == "GET":
        return render_template("add_word.html")

    # get words from HTML form. 
    if request.method == "POST":

        words_length = len(Word.query.filter_by(user_id = session['id']).all())
        if words_length >= 10:
            return redirect("/show_words")

        timestamp = "%s - %s" % (get_date(), get_time())
        new_word = request.form.get("new_word")
        user_id = session['id']
        part_of_speech = request.form.get("part_of_speech")
        translation = request.form.get("translation")
        sentence = request.form.get("sentence")

        # create Word object for the dictionary 
        new_word_entry = Word(timestamp = timestamp, word = new_word, user_id = user_id, part_of_speech = part_of_speech, translation = translation, sentence = sentence)

        # add word object to database
        db.session.add(new_word_entry)
        db.session.commit()

        # set word count after adding new word to keep make sure they are under the word limit
        session['current_word_count'] = len(Word.query.filter_by(user_id = session['id']).all())
        print(session['current_word_count'])

        return redirect("/show_words")

# get word from delete button and delete from database
@app.route("/delete_word/<id>", methods=["GET","DELETE"])
def delete_word(id):
    Word.query.filter_by(id=id).delete()
    db.session.commit()
    print(id)
    return redirect("/show_words")


    