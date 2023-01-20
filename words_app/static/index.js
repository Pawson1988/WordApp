import copyToClipboard from "./copy_to_clipboard.js"
import resetCardPositions from "./reset_card_positions.js"



// only execute code below if on /get_translation page
if(window.location.pathname === "/get_translation"){
    const translatedTextEl = document.querySelector("#translated_text")
    const copyBtn = document.querySelector(".copy_btn")

    copyBtn.addEventListener("click", function(){
        copyToClipboard(translatedTextEl)
})}


const cards = document.querySelectorAll(".card-multiple")
const chosen_words = document.querySelector(".chosen_words")
const clear_words_button = document.querySelector(".clear_words_btn")




for(let card of cards){
    
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
    chosen_words.textContent = "No Words"
    for(let card of cards){
        resetCardPositions(card)
    }
})

