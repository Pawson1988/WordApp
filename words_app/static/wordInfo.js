const wordFromCard = document.querySelectorAll(".card-header")
const definitionDiv = document.querySelector(".definitionDiv")
const pronunciationDiv = document.querySelector(".pronunciationDiv")
const synonymDiv = document.querySelector(".synonymDiv")

class WordInfo{

    static wordDef;
    
    static resetWordInfoDivs(){
        definitionDiv.textContent = ""
        pronunciationDiv.textContent = ""
        synonymDiv.textContent = ""
    }

    static getWordInfo(word){
        fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${word}`)
        .then((response) => response.json())
        .then((data) => {
            WordInfo.wordDef = data
            WordInfo.showWordInfo(WordInfo.wordDef)
        })
        .catch((err) => console.log(err));
    }

    static toggleWordInfo(){
        let clicked
            for(let word of wordFromCard){
                word.addEventListener("click", function(e){
                e.stopImmediatePropagation()
                WordInfo.removeAllBgColors(wordFromCard)
                if(clicked != true){
                    clicked = true
                    word.style.backgroundColor = "rgb(0, 204, 255)"
                    WordInfo.getWordInfo(word.textContent)
                } else {
                    clicked = false
                    WordInfo.resetWordInfoDivs()
                }
            })
        }   
    }

    static removeAllBgColors(elements){
        for(let element of elements){
            element.style.removeProperty("background-color")
        }
    }
   
    static showWordInfo(wordDef){
        definitionDiv.textContent = `Definition: ${wordDef[0].meanings[0].definitions[0].definition}`
        pronunciationDiv.textContent = `Pronunciation: ${wordDef[0].phonetic}`
        synonymDiv.textContent = `Synonym(s): ${wordDef[0].meanings[0].definitions[0].synonyms}`
    }
}

export { WordInfo }

