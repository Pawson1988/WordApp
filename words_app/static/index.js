import copyToClipboard from "./copy_to_clipboard.js"



// only execute code below if on /get_translation page
if(window.location.pathname === "/get_translation"){
    const translatedTextEl = document.querySelector("#translated_text")
    const copyBtn = document.querySelector(".copy_btn")

    copyBtn.addEventListener("click", function(){
        copyToClipboard(translatedTextEl)
})}


const cards = document.querySelectorAll(".card-multiple")
const chosen_words = document.querySelector(".chosen_words")
const card_header = document.querySelectorAll(".card-header")
const clear_words_button = document.querySelector(".clear_words_btn")

console.log(cards)

function resetCardPositions(card){
    card.style.postion = "relative"
    card.style.top = "0"
    card.style.zIndex = "0"
}

let index = 0
for(let card of cards){
    index++
    card.addEventListener("click", () => {
        if(card.style.top != "10rem"){
           console.log(card)
            chosen_words.textContent += `${card.childNodes[1].textContent} `
            card.style.position = "relative"
            card.style.top = "10rem"
            card.style.zIndex++  
            chosen_words.style.marginTop = "10rem"
        } else {
            resetCardPositions(card)
        }
    })
}

clear_words_button.addEventListener("click", () => {
    chosen_words.textContent = ""
    for(let card of cards){
        resetCardPositions(card)
    }
})

