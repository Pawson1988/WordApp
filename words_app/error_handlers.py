from words_app import app

from flask import render_template, abort, request

@app.errorhandler(404)
def not_found(e):
    error_text = "Sorry, the page you are looking for doesn't seem to exit for some reason, maybe it went on holiday......"
    return render_template("error_template.html", error_text = error_text)


@app.errorhandler(500)
def server_error(e):
    app.logger.error(f'Error: {e}, route: {request.url}')
    error_text = "There is a server error, please get in touch with the administrator"
    return render_template("error_template.html", error_text = error_text)

