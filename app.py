from flask import Flask, render_template, request, redirect, session
from flask_session import Session 
from flask_sqlalchemy import SQLAlchemy
from helpers.translation_request import translate_word
from helpers.date_and_time import get_date

app = Flask(__name__)


# change to name of your database; add path if necessary
db_name = 'words.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True



# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

# configure session
app.config['SESSION_PERMANENT'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = 300 # set each session to timeout after 5 minutes in development.
app.config['SESSION_TYPE'] = "filesystem"

Session(app)

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))

# Create the model for the DB
class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id))
    word = db.Column(db.String(30))
    part_of_speech = db.Column(db.String, nullable=False)
    translation = db.Column(db.String(40))
    sentence = db.Column(db.String(150))


# Add create_all() to app context and add the above models to the database
with app.app_context():
    # db.drop_all()
    db.create_all()

user_accounts = [
    {"username": "james", "password": "James"},
    {"username": "claudia", "password": "Claudia"},
    {"username": "david", "password": "David"}
]

# add users above to database
with app.app_context():
    if not User.query.all():
        for user in user_accounts:
            new_user = User(username = user['username'], password = user['password'])
            db.session.add(new_user)
            db.session.commit()



# template word to show on show_words page 
default_words = [
    {"timestamp": get_date(), "word": "new", "user_id": 1, "part_of_speech": "adjective", "translation": "nuevo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": get_date(), "word": "old", "user_id": 2, "part_of_speech": "adjective", "translation": "antiguo", "sentence": "This is an example of a sentence using this word"},
    {"timestamp": get_date(), "word": "book", "user_id": 3, "part_of_speech": "noun", "translation": "libro", "sentence": "This is an example of a sentence using this word"}
]

# Add default word to database when app is run
with app.app_context():
    if not Word.query.all(): # if there isn't a word in the dictionary add the word(s) below
        for word in default_words:
            new_word_entry = Word(
            timestamp = word['timestamp'],
            word = word['word'], user_id = word['user_id'], 
            part_of_speech = word['part_of_speech'], 
            translation = word['translation'], 
            sentence = word['sentence']
            )
            db.session.add(new_word_entry)
            db.session.commit()

@app.before_request
def is_logged_in():
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
        timestamp = get_date()
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

if __name__ == "__main__":
    app.run(debug=True)

    