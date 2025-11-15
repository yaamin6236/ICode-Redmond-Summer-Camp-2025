import {toBase, uplodFile,} from "./aicamp_day3/ai_camp_day3.js";


let input = document.querySelector(".user-input")
let submit = document.querySelector(".submit")

async function query(data) {
    const response = await fetch(
        "https://api-infrence.huggingface.co/modles/stabilityai/stable-diffusion-xl-base-1.0",
        {
            headers: {Autherization: "bearer <token_here>"},
            method: "POST",
            body: JSON.stringify(data)
        }
    );
     const result = await response.blob();
     return result;
    }
    
    query({"inputs":"cowboy"}).then(async(response) => {
        let base64 = await toBase64(response) 
        let imageURL = await uploadFile(base64)
        console.log(imageUrl)

        let img = document.createElement('img')
        img.src = imageUrl
        document.body.appendChild(img)
    
        
    });

    submit.addEventListener("click", () => {
          if(input.value != ""){
            query({ response_format: "b64_json",
                promt: 'chicken wearing a suit',
                model: "stability-ai/sdxl",})
            .then(async (response) => {

                let imageURL = await uploadFile(reponse)
                console.log(imageURL)

                let img = document.createElement('img')
                img.src = imageURL
                document.body.appendChild(img)
            });

        }

          
    });
   
    


