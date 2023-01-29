from words_app import app
from flask import request, render_template, redirect
from helpers.translation_request import translate_word


# translate phrase and sho it on translation.html page 
@app.route("/get_translation", methods=['GET','POST'])
def get_translation():
    text = "No Text"
    translated = "No translation"
    if request.method == 'POST':
        text = request.form.get("word_to_translate")
        lang = request.form.get("lang")
        translated = translate_word(text, lang)
    return render_template("/translation.html", translation = translated, original_text = text)


# translate word on add_word page 
@app.route("/word_translation", methods=["POST"])
def word_translation():
    word_info = {}
    if request.method == "POST":
        print(request.form)
        if request.form.get("hidden_word"):
            word_info["part_of_speech"] = request.form.get("hidden_part_of_speech")
            word_info["sentence"] = request.form.get("hidden_sentence")
            print(word_info["sentence"])
            word_info["word_to_translate"] = request.form.get("hidden_word")
            word_info["translated_word"] = translate_word(word_info["word_to_translate"], "ES")
            return render_template("add_word.html", word_info = word_info)
        return redirect("add_word")