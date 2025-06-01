import requests
from django.core.mail import send_mail

from config import settings
from config.settings import BOT_TOKEN, TELEGRAM_URL

RARE_FEE = 0.1
EXPENSIVE_FEE = 0.05
NO_FEATURES_FEE = 0.02


def send_telegram_message(client_tg_chat_id, message):
    """Function to send a message to user via Telegram"""

    params = {
        "text": message,
        "chat_id": client_tg_chat_id,
    }
    requests.get(f"{TELEGRAM_URL}{BOT_TOKEN}/sendMessage", params=params)


def send_email_message(users_list, book, message):
    """Function to send a message to user via Mail"""

    send_mail(
        subject=f"Updated info about book '{book}'",
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=users_list,
    )
