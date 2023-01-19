from words_app import app
from words_app import db
from helpers.date_and_time import get_date

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