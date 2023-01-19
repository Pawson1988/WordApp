from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

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

from words_app import routes
