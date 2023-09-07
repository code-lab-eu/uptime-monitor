import requests
import os
import ast

from datetime import timedelta
from dotenv import load_dotenv


def notify_telegram(message):
    api_token = os.getenv("API_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    api_url = f'https://api.telegram.org/bot{api_token}/sendMessage'
    requests.post(api_url, json={'chat_id': chat_id, 'text': message})


def check_sites():
    for url in ast.literal_eval(os.getenv("URLS")):
        try:
            website_url = requests.get(url, timeout=30)
            if website_url.status_code != 200:
                notify_telegram(f"%s is down" % url)
            else:
                if website_url.elapsed > timedelta(seconds=int(os.getenv("TIMEOUT"))):
                    notify_telegram(f"%s is slow" % url)

        except Exception as e:
            notify_telegram(str(e))


load_dotenv()
check_sites()
