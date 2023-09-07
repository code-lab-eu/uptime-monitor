import requests
import os
import ast

from dotenv import load_dotenv
def check_sites():
    load_dotenv()
    apiToken = os.getenv("API_TOKEN")
    chatID = os.getenv("CHAT_ID")
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
    for url in ast.literal_eval(os.getenv("URLS")):
        try:
            website_url = requests.get(url, timeout=3)
            if website_url.status_code != 200:
                requests.post(apiURL, json={'chat_id': chatID, 'text': f"%s is down" % url})
        except Exception as e:
            requests.post(apiURL, json={'chat_id': chatID, 'text': str(e)})

check_sites()
