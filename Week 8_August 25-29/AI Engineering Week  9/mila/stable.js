import { tobase64, uploadfile } from "./ai_camp_day3.js";

let input=document.querySelector('.user-input');
let subment=document.querySelector('.submit');

async function query(data) {

    const response = await fetch(

        "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-x1-base-1.0",

        {

            headers: { authorization: "bearer <token_here>" },

            method: "POST"

            body: JSON.stringify(data),

        }

    );

    const result = await response.blob();

    return result;

}

query({"inputs": "cowboy"}).then(async (response) => {



    let base64 = await tobase64(response)

    let imageURL = await uploadfile(base64)

    console.log(imageURL)



    let img = document.createElement('img')

    img.src = imageURL

    document.body.appendChild(img)
});

subment.addEventListener('click',()=>{

});


Conversation with Gemini

import { tobase64, uploadfile } from "./ai_camp_day3.js";



let input = document.querySelector(".user-input")

let submit = document.querySelector(".submit")





async function query(data) {

    const response = await fetch(

        "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-x1-base-1.0",

        {

            headers: { authorization: "bearer <token_here>" },

            method: "POST"

            body: JSON.stringify(data),

        }

    );

    const result = await response.blob();

    return result;

}

query({"inputs": "cowboy"}).then(async (response) => {



    let base64 = await tobase64(response)

    let imageURL = await uploadfile(base64)

    console.log(imageURL)



    let img = document.createElement('img')

    img.src = imageURL

    document.body.appendChild(img)

});



submit.addEventListener("click", () => {

});

submit.addEventListener("click",  () => {

    if(input.value != "")}

    query({ response_format: b64_json

        prompt: 'chicken wearing a suit'

        model: "stability-ai/sdxl", })

        .then(async (response) => {



            let imageURL = await uploadfile(response)

            console.log(imageURL)



             let img = document.createElement('img')

             img.src = imageURL

             document.body.appendChild(img)

        });

    }

});