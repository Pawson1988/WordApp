import os
from dotenv import load_dotenv
load_dotenv("../.env")

def translate_word(text, lang):
    import deepl 
    auth_key = os.environ.get("deepL_auth_key")
    translator = deepl.Translator(auth_key) 
    result = translator.translate_text(text, target_lang = lang) 
    translated_text = result.text
    return translated_text
