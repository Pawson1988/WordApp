import copyToClipboard from "./copy_to_clipboard.js"

const translatedTextEl = document.querySelector("#translated_text")
const copyBtn = document.querySelector(".copy_btn")


copyBtn.addEventListener("click", function(){
    copyToClipboard(translatedTextEl)
})