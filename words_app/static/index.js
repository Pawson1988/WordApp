import copyToClipboard from "./copy_to_clipboard.js"
import wordsSentenceCheck from "./words_sentence_check.js"



// only execute code below if on /get_translation page
if(window.location.pathname === "/get_translation"){
    const translatedTextEl = document.querySelector("#translated_text")
    const copyBtn = document.querySelector(".copy_btn")

    copyBtn.addEventListener("click", function(){
        copyToClipboard(translatedTextEl)
})}
// end of /get_translation code

wordsSentenceCheck()

const wordFromCard = document.querySelectorAll(".card-header")
const definitionDiv = document.querySelector(".definitionDiv")
const pronunciationDiv = document.querySelector(".pronunciationDiv")
const synonymDiv = document.querySelector(".synonymDiv")

function resetWordInfoDivs(){
        definitionDiv.textContent = ""
        pronunciationDiv.textContent = ""
        synonymDiv.textContent = ""
}

let wordDef;

function showDefinitionAndPhonetics(wordDef){
    definitionDiv.textContent = `Definition: ${wordDef[0].meanings[0].definitions[0].definition}`
    pronunciationDiv.textContent = `Pronunciation: ${wordDef[0].phonetic}`
    synonymDiv.textContent = `Synonym(s): ${wordDef[0].meanings[0].definitions[0].synonyms}`
}

function getWordDefinition(word){
    fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${word}`)
    .then((response) => response.json())
    .then((data) => {
        wordDef = data
        showDefinitionAndPhonetics(wordDef)
    })
    .catch((err) => console.log(err));

    
}

function removeAllBgColors(elements){
    for(let element of elements){
        element.style.removeProperty("background-color")
    }
}

let clicked
for(let word of wordFromCard){
    word.addEventListener("click", function(e){
        e.stopImmediatePropagation()
        removeAllBgColors(wordFromCard)
        if(clicked != true){
            clicked = true
            word.style.backgroundColor = "rgb(0, 204, 255)"
            getWordDefinition(word.textContent)
        } else {
            clicked = false
            resetWordInfoDivs()
        }
    })
}
// export the dictionry information divs so that we can clear the div with the reset buttion from words_sentence_check.js
export {resetWordInfoDivs}
