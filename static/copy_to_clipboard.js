
export default function copyToClipboard(text){
    // get text from element
    let copyText = text.textContent

   // copy the text to clipboard
    navigator.clipboard.writeText(copyText);

  // Alert the copied text
    alert("Copied the text: " + copyText);
}