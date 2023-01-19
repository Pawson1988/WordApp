import copyToClipboard from "./copy_to_clipboard.js"



// only execute code below if on /get_translation page
if(window.location.pathname === "/get_translation"){
    const translatedTextEl = document.querySelector("#translated_text")
    const copyBtn = document.querySelector(".copy_btn")

    copyBtn.addEventListener("click", function(){
        copyToClipboard(translatedTextEl)
})}


const cards = document.querySelectorAll(".card-multiple")

console.log(cards)

for(let card of cards){
    card.addEventListener("click", () => {
        if(card.style.top != "10rem"){
           console.log(card)
            card.style.position = "relative"
            card.style.top = "10rem"
            card.style.zIndex++  
        } else {
            card.style.postion = "relative"
            card.style.top = "0"
            card.style.zIndex = "0"
        }
       
    })
}

