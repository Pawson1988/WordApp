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



if(window.location.pathname === "/add_word" || window.location.pathname === "/word_translation"){

    const hiddenWordInput = document.querySelector(".hidden_word")
    const hiddenSentence = document.querySelector(".hidden_sentence")
    const hiddenPartOfSpeech = document.querySelector(".hidden_part_of_speech")

    const newWordInput = document.querySelector(".new_word")
    const partOfSpeech = document.querySelector(".part_of_speech")
    const addWordSentence = document.querySelector(".add_word_sentence")

    newWordInput.addEventListener("input", function(e){
        hiddenWordInput.value = newWordInput.value.trim()
    })

    partOfSpeech.addEventListener("change", function(e){
        hiddenPartOfSpeech.value = partOfSpeech.value
    })

    addWordSentence.addEventListener("input", function(e){
        hiddenSentence.value = addWordSentence.value
    })
}
