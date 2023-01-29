from words_app import app
from words_app import db
from helpers.default_data import user_accounts, default_words

# create DB model for User
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))

    def __repr__(self):
        return f'username: {self.username}'

# Create the model for the word DB
class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id))
    word = db.Column(db.String(30))
    part_of_speech = db.Column(db.String, nullable=False)
    translation = db.Column(db.String(40))
    sentence = db.Column(db.String(150))

    def __repr__(self):
        return f'id: {self.id} - word: {self.word} - Date and time created: {self.timestamp}'


# Add create_all() to app context and add the above models to the database
with app.app_context():
    # db.drop_all()
    db.create_all()



# add users above to database
with app.app_context():
    if not User.query.all():
        for user in user_accounts:
            new_user = User(username = user['username'], password = user['password'])
            db.session.add(new_user)
            db.session.commit()


# Add default words to database when app is run
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