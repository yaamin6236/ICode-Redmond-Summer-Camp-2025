import { toBase64, uploadFile } from "./aicamp_day3/ai_camp_day3.js";

let input = document.querySelector(".user-input")
let submit = document.querySelector(".submit")

async function query(data) {
        const response = await fetch(
                "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0",
                {
                        headers: { Authorization: "Bearer YOUR_HUGGING_FACE_TOKEN" },  // Replace with your token
                        method: "POST",
                        body:  JSON.stringify(data),
                }
        );
        const result = await response.blob();
        return result;
    }
    query({"inputs": "cowboy"}).then(async (response) => {
        let base64 = await toBase64(response)
        letimageURL = await uploadFile(base64)
        console.log(imageURL)
        let img = document.createElement('img')
        img.src = imageURL
        document.body.appendChild(img)
    });

    submit.addEventListener("click", () => {
        if(input.value != ""){
            query({         response_format: "b64_json",
                            prompt: 'chicken wearing a suit',
                            model: "stability-ai/sdxl", })
                .then(async (response) => {
                
                let imageURL = await uploadFile(response)
                console.log(imageURL)

                let img = document.createElement('img')
                img.src = imageURL
                document.body.appendChild(img)
                });
        }
    });