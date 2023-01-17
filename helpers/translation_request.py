

def translate_word(text, lang):
    import deepl 
    auth_key = 'ac64dbf1-9030-61f2-ddfe-609c775d110a:fx'
    translator = deepl.Translator(auth_key) 
    result = translator.translate_text(text, target_lang = lang) 
    translated_text = result.text
    return translated_text
