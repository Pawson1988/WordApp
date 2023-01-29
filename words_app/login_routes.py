from words_app import app
from words_app.models import User, Word
from flask import session, redirect, request, render_template
from helpers.date_and_time import get_date, get_time


@app.before_request
def is_logged_in():
    # save date and time in each request to show in nav bar
    session['date'] = get_date()
    session['time'] = get_time()
    
    if request.endpoint != "login" and request.endpoint != "static" and request.endpoint != "favicon.ico":
        # if url is not login or static
        # save previous url in session to redirect back to the same page after login 
        session['url'] = request.url
        if not session.get('username'):
            return redirect('/login')

# login route 
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    if request.method == 'POST':
        username = request.form.get("username") or "no username given"
        password = request.form.get("password") or "no password given"
        current_user = User.query.filter_by(username = username).first()

        # check current_user to handle not finding a user in the database
        if current_user and  username == current_user.username and password == current_user.password:
            session.permanent = True
            session['username'] = username
            session['id'] = current_user.user_id 
            session['current_word_count'] = len(Word.query.filter_by(user_id = session['id']).all())
            print(session['current_word_count'])
            return redirect("/show_words")
        else:
            # log an incorrect login with username, time and date, return imediately back to login
            warning = "Please use a correct username and/or password"
            app.logger.error(f"{username} tried logging in but doesn't exist at {get_time()} on {get_date()}")
            return render_template("/login.html", warning = warning)

# logout route
@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect("/login")