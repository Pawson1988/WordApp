from words_app import app
from words_app.models import User, Word
from flask import render_template, request, redirect, session

from helpers.translation_request import translate_word
from helpers.date_and_time import get_date, get_time




@app.before_request
def is_logged_in():
    session['date'] = get_date()
    session['time'] = get_time()
    if request.endpoint != "login" and request.endpoint != "static":
     if not session.get('username'):
        return redirect('/login')

     

@app.route("/get_translation", methods=['GET','POST'])
def get_translation():
    translated = "No translation"
    if request.method == 'POST':
        text = request.form.get("word_to_translate")
        lang = request.form.get("lang")
        translated = translate_word(text, lang)
    return render_template("/translation.html", translation = translated)

    

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

# login route 
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        current_user = User.query.filter_by(username = username).first()
        print(current_user.username)

        if username == current_user.username and password == current_user.password:
            session.permanent = True
            session['username'] = username
            session['date'] = get_date()
            session['id'] = current_user.user_id 
            return redirect("/show_words")
        else:
            return redirect("/login")

# logout route
@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect("/login")

# First route to show the form
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

        return redirect("/show_words")

# get word from delete button and delete from database
@app.route("/delete_word/<id>", methods=["GET","DELETE"])
def delete_word(id):
    Word.query.filter_by(id=id).delete()
    db.session.commit()
    print(id)
    return redirect("/show_words")