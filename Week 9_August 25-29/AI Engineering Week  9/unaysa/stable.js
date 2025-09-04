import {uploadFile } from "./aicamp_day3/ai_camp_day3.js";

let input = document.querySelector(".user-input")
let submit = document.querySelector(".submit")


async function query(data) {
	const response = await fetch(
    "https://router.huggingface.co/nebius/v1/images/generations", {
      method: "POST",
      headers: {
        Authorization: `Bearer <token-here>`, 
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        prompt: `${data.inputs}`,
        response_format: "b64_json",
        model: "stability-ai/sdxl",
      }),
    }
  );
	const jsonResponse = await response.json();
	console.log(jsonResponse)
	const base64String = jsonResponse.data[0].b64_json; 
	const mimeType = 'image/png'; 
  	const base64DataUri = `data:${mimeType};base64,${base64String}`;
	return base64DataUri;
}


submit.addEventListener("click", () => {
	if(input.value != ""){
		query({"inputs": input.value}).then(async (response) => {

			let imageURL = await uploadFile(response)
			console.log(imageURL)
		
			let img = document.createElement('img')
			img.src = imageURL 
			document.body.appendChild(img) 
		});
	}
}); 