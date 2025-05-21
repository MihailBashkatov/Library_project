import requests

from config.settings import BOT_TOKEN, TELEGRAM_URL


def send_telegram_message(telegram_chat_id, message):
    """Function to send a message to user via Telegram"""

    params = {
        "text": message,
        "chat_id": telegram_chat_id,
    }
    requests.get(f"{TELEGRAM_URL}{BOT_TOKEN}/sendMessage", params=params)
