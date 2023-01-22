import resetCardPositions from "./reset_card_positions.js"
import is_correct_Sentence from "./is_correct_Sentence.js"
import {definitionDiv, pronunciationDiv, synonymDiv} from "./index.js"

export default function wordsSentenceCheck(){

// Get the elements from the DOM tree
const cards = document.querySelectorAll(".card-multiple")
const chosen_words = document.querySelector(".chosen_words")
const clear_words_button = document.querySelector(".clear_words_btn")
const sentence = document.querySelector(".sentence")
const check_btn = document.querySelector(".check_sentence")

// Initialise array for selected words from word list to use later
let selectedWords = []

function addWordToChosenWords(array){
    while (chosen_words.firstChild) {
        chosen_words.removeChild(chosen_words.lastChild);
    }

    for(let item in array){
        let wordDiv = document.createElement("div")
        wordDiv.textContent = array[item]
        wordDiv.setAttribute("class", "word-div")
        chosen_words.appendChild(wordDiv)
    }
}

// function for when user is selecting cards
for(let card of cards){
    card.addEventListener("click", () => {
        if(card.style.top != "5rem"){
            selectedWords.push(card.childNodes[1].textContent)
            card.style.position = "relative"
            card.style.top = "5rem"
            card.style.zIndex++  
            chosen_words.style.marginTop = "5rem"
        } else {
            resetCardPositions(card)
            let index = selectedWords.indexOf(card.childNodes[1].textContent)
            if(index > -1){
                selectedWords.splice(index, 1)   
            }
            
        }
        addWordToChosenWords(selectedWords)
    })
}

sentence.addEventListener("keyup", () => {
    if(sentence.value === ""){
        sentence.style.backgroundColor = "rgba(98, 172, 112, 0.4)"
    }
})

// reset everything function
clear_words_button.addEventListener("click", () => {
    for(let card of cards){
        resetCardPositions(card)
        definitionDiv.textContent = ""
        pronunciationDiv.textContent = ""
        synonymDiv.textContent = ""
        selectedWords = []
        sentence.value = ""
        sentence.style.backgroundColor = "rgba(98, 172, 112, 0.4)"
        addWordToChosenWords(selectedWords)
    }
})

// check whether the sentence the user inputted contains the words they selected and is a good gramatical sentence. 
check_btn.addEventListener("click", () => {
    if(sentence.value){
        let isEvery = selectedWords.every(item => sentence.value.toLowerCase().includes(item.toLowerCase()))
        if(isEvery && is_correct_Sentence(sentence.value)){
            sentence.style.backgroundColor = "green"
        } else {
            sentence.style.backgroundColor = "red"
        }
    }
})
}