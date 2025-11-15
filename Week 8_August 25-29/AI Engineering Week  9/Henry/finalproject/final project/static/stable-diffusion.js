import {contentFilterText, toBase64, uploadFile, downloadableLink} from "./content-filter.js";
import { hugging_face_key } from "./keys.js";

const submitButton = document.querySelector(".submit-btn"); 
const downloadButton = document.querySelector(".download-btn");
const downloadLink = document.querySelector(".download-link");
const imageFrame = document.querySelector(".image-frame"); 
const entry = document.querySelector(".image-gen-entry");
const displayH1 = document.createElement('h1'); 

export let inputDisplay;

/** query function **********************************
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * ***************************************************/

downloadButton.addEventListener('click', () => {
	if(imageFrame.hasChildNodes() == true && downloadableLink != null)
	{
		downloadLink.href = downloadableLink;
		downloadLink.download = "image.png";
	}
})

submitButton.addEventListener('click', () =>{
	if(imageFrame.hasChildNodes() == true){
		imageFrame.removeChild(...imageFrame.children); 
	}
	submitClicked(); 
});

async function submitClicked(){
	const input = entry.value;
	if(input != ""){
		inputDisplay = input;
		let contentValue = await contentFilterText(input);
		
		if(contentValue == 1){
			const img = document.createElement('img'); 
			img.classList.add('image-frame-loading'); 
			img.src = "../../static/asset/image-loading.gif"; 
			imageFrame.appendChild(img); 
			/***********************************
			 * 
			 * 
			 * 
			 * 
			 * 
			 * 
			 * 
			 * 
			 * 
			 * 
			 *********************************/
			entry.value = "";
			entry.placeholder = "Type something in..."
		}else{
			if(contentValue == 0){
				entry.value = "";
				entry.placeholder = "Please be appropriate!"; 
				inputDisplay = "Please be appropriate!"
			}else{
				entry.value = "";
				entry.placeholder = "There has been an error.";
				inputDisplay = "There has been an error." 
			}
		}
		display_input("");
	}
	
}

export function display_input(input){
	displayH1.textContent = input;
	imageFrame.appendChild(displayH1);
}
