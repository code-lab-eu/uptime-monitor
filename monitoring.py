import requests
import os
from dotenv import load_dotenv
def send_to_group_telegram(group_message):
    load_dotenv()
    apiToken = os.getenv("API_TOKEN")
    chatID = os.getenv("CHAT_ID")
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': group_message})
        print(response.text)
    except Exception as e:
        print(

send_to_group_telegram("Hello!")