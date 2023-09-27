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
    # The number of times to check
    max_attempts = 3
    for url in ast.literal_eval(os.getenv("URLS")):
        # Initialize a flag to track the type of issue (down or slow)
        problems = []
        for attempt in range(max_attempts):
            try:
                website_url = requests.get(url, timeout=10)
                if website_url.status_code != 200:
                    problems.append("down")
                elif website_url.elapsed > timedelta(seconds=int(os.getenv("TIMEOUT"))):
                    problems.append("slow")
                else:
                    problems = []
                    break
            except Exception as e:
                problems.append(str(e))
        if len(problems):
            problems = ', '.join(problems)
            notify_telegram(f"{url} is {problems}")


load_dotenv()
check_sites()
