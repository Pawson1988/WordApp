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

const wordFromCard = document.querySelectorAll(".card-header")

let wordDef;

function getWordDefinition(word){
    fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${word}`)
    .then((response) => response.json())
    .then((data) => {
        wordDef = data
        console.log(wordDef[0].phonetics[0].text)
    })
    .catch((err) => console.log(err));

    
}

for(let word of wordFromCard){
    word.addEventListener("click", function(e){
        e.stopImmediatePropagation()
        getWordDefinition(word.textContent)
    })
}


