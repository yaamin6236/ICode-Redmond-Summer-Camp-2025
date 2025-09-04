import requests

def make_text(text):
    text_input = text[0]["generated_text"]
    data = {
        'text': text_input,
        'lang': 'en',
        'opt_countries': 'us,gb,fr',
        'mode': 'rules',
        'api_user': '1820253693',
        'api_secret': 'Yc42azkarSBjGDhqiAHkZNEojyQfB7tm'
    }

    try:
        response = requests.post('https://api.sightengine.com/1.0/text/check.json', data=data)
        response_data = response.json()
        if response_data.get('profanity', {}).get('matches'):
            return "Content Blocked." 
        else:
            return text_input
    except Exception as error:
        print("Error in content_filter_text:", error)
        raise error
