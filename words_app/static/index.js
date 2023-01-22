import copyToClipboard from "./copy_to_clipboard.js"
import wordsSentenceCheck from "./words_sentence_check.js"



// only execute code below if on /get_translation page
if(window.location.pathname === "/get_translation"){
    const translatedTextEl = document.querySelector("#translated_text")
    const copyBtn = document.querySelector(".copy_btn")

    copyBtn.addEventListener("click", function(){
        copyToClipboard(translatedTextEl)
})}

wordsSentenceCheck()


