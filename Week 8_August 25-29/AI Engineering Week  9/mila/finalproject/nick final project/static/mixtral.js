import { contentFilterText, stopAtLastPeriod, removeBlankLines } from "./content-filter.js";
import { hugging_face_key } from "./keys.js";

const submitButton = document.querySelector(".submit-btn");
const entry = document.querySelector(".image-gen-entry");
const textFrame = document.querySelector(".text-frame");
const downloadButton = document.querySelector(".download-btn");
const downloadableLink = document.querySelector(".download-link");

let records = [];

/*query function****************************
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
******************************************/

downloadButton.addEventListener('click', () => {
    const filename = "records.txt";
    let conversation = "";
    if (records.length > 0) {
        records.forEach(record => {
            conversation += record + '\n' + '\n';
        });

        const blob = new Blob([conversation], {
            type: 'text/plain;charset=utf-8'
        });
        downloadableLink.download = filename;
        downloadableLink.href = window.URL.createObjectURL(blob);
    }
})


submitButton.addEventListener('click', () => {
    submit();
});

async function submit() {
    const input = entry.value;
    if (input != "") {
        let contentValue = await contentFilterText(input);
        if (contentValue == 1) {
            query({ "inputs": input, "parameters": { "return_full_text": false } }).then(async (response) => {
                let aiContentValue = await contentFilterText(response[0].generated_text);
                if (aiContentValue == 1) {
                    /*****************************
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
                     **********************************/
                } else {
                    setPlaceholder(aiContentValue);
                }
            });
        } else {
            setPlaceholder(contentValue);
        }

    }

}


function setPlaceholder(cv) {
    if (cv == 0) {
        entry.value = "";
        entry.placeholder = "Please be appropriate!";
    } else {
        entry.value = "";
        entry.placeholder = "There has been an error.";
    }
}


