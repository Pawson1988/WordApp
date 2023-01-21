import copyToClipboard from "./copy_to_clipboard.js"
import resetCardPositions from "./reset_card_positions.js"
import is_correct_Sentence from "./is_correct_Sentence.js"



// only execute code below if on /get_translation page
if(window.location.pathname === "/get_translation"){
    const translatedTextEl = document.querySelector("#translated_text")
    const copyBtn = document.querySelector(".copy_btn")

    copyBtn.addEventListener("click", function(){
        copyToClipboard(translatedTextEl)
})}

// Get the elements from the DOM tree
const cards = document.querySelectorAll(".card-multiple")
const chosen_words = document.querySelector(".chosen_words")
const clear_words_button = document.querySelector(".clear_words_btn")
const sentence = document.querySelector(".sentence")
const check_btn = document.querySelector(".check_sentence")

// Initialise array for selected words from word list to use later
let selectedWords = []

// function for when user is selecting cards
for(let card of cards){
    card.addEventListener("click", () => {
        if(card.style.top != "10rem"){
           console.log(card)
            chosen_words.textContent += `${card.childNodes[1].textContent} `
            selectedWords.push(card.childNodes[1].textContent)
            console.log(selectedWords)
            card.style.position = "relative"
            card.style.top = "10rem"
            card.style.zIndex++  
            chosen_words.style.marginTop = "10rem"
        } else {
            resetCardPositions(card)
            selectedWords = []
        }
    })
}

// reset everything function
clear_words_button.addEventListener("click", () => {
    chosen_words.textContent = ""
    for(let card of cards){
        resetCardPositions(card)
        selectedWords = []
        sentence.value = ""
        sentence.style.backgroundColor = "rgba(98, 172, 112, 0.4)"
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


