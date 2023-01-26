import copyToClipboard from "./copy_to_clipboard.js"
import wordsSentenceCheck from "./words_sentence_check.js"
import { WordInfo } from "./wordInfo.js"

// only execute code below if on /get_translation page
if(window.location.pathname === "/get_translation"){
    const translatedTextEl = document.querySelector("#translated_text")
    const copyBtn = document.querySelector(".copy_btn")

    copyBtn.addEventListener("click", function(){
        copyToClipboard(translatedTextEl)
})}
// end of /get_translation code

// check sentence for grammar
if(window.location.pathname === "/show_words"){
    wordsSentenceCheck()

// toggle word info when car-header is clicked
WordInfo.toggleWordInfo()
}


const hiddenWordInput = document.querySelector(".hidden_word")
const newWordInput = document.querySelector(".new_word")

console.log(hiddenWordInput, newWordInput)

newWordInput.addEventListener("change", function(e){
    hiddenWordInput.value = newWordInput.value
})

