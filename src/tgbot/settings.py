from os import getenv
from os import getenv
from webbrowser import get
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(usecwd=True, filename="private/tokens.txt"))

GITHUB_TOKEN = getenv('GITHUB_TOKEN')
TELEGRAM_TOKEN = getenv('TELEGRAM_TOKEN')

if __name__ == "__main__":
    print(f"GITHUB_TOKEN: {GITHUB_TOKEN}")
    print(f"TELEGRAM_TOKEN: {TELEGRAM_TOKEN}")