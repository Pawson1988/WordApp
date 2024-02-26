
const definitionDiv = document.querySelector(".definitionDiv")
const pronunciationDiv = document.querySelector(".pronunciationDiv")
const wordFromCard = document.querySelectorAll(".card-header")

async function fetchWithTimeout(resource, options = {}) {
    const { timeout = 8000 } = options;
    
    const controller = new AbortController();
    const id = setTimeout(() => controller.abort(), timeout);
    const response = await fetch(resource, {
      ...options,
      signal: controller.signal  
    });
    clearTimeout(id);
    return response;
}

class WordInfo{
    
    wordDef;

    static resetWordInfoDivs(){
        definitionDiv.textContent = "" 
        pronunciationDiv.textContent = ""
    }

    static async getWordInfo(word){
        //fetch(``)
        fetchWithTimeout(`https://api.dictionaryapi.dev/api/v2/entries/en/${word}`, {timeout: 1500})
        .then((response) => response.json())
        .then((data) => {
            this.wordDef = data
            WordInfo.showWordInfo(this.wordDef)
        })
        .catch((err) => {
          console.log(err)
          WordInfo.showWordInfo(null)
        });
    }

    static removeAllBgColors(elements){
        for(let element of elements){
            element.style.removeProperty("background-color")
        }
    }
   
    static showWordInfo(wordDef){
        if(wordDef != null){
            definitionDiv.textContent =  `Definition: ${wordDef[0]?.meanings[0].definitions[0].definition}`
            pronunciationDiv.textContent =  `Pronunciation: ${wordDef[0]?.phonetic}` 
        } else {
            definitionDiv.textContent = `Not Working`
            pronunciationDiv.textContent = `Not Working`
        }
        
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
}

export { WordInfo }

