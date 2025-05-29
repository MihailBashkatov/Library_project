# import datetime
from datetime import timedelta

from celery import shared_task
from django.utils import timezone
from django.utils.timezone import localtime

from books.models import BookDetail
from books.overdue_fees import EXPENSIVE_FEE, NO_FEATURES_FEE, RARE_FEE
from books.services import send_telegram_message


@shared_task
def send_tg_message_book(client_tg_chat_id, book, due_date=False, renewed=False):
    """Task to send Telegram message, if user took, renew or return a book"""

    # Message for returning a book
    if not due_date:
        message = f'Thanks. you returned a book "{book}". Welcome again'

    # Message to renew a book
    elif renewed:
        message = f'Thanks. you renewed a book "{book}". New Due date is {due_date.strftime("%Y-%m-%d")}'

    # Message to take a book
    else:
        message = f'Thanks. you received a book "{book}". Due date is {due_date.strftime("%Y-%m-%d")}'

    try:
        send_telegram_message(client_tg_chat_id, message)
    except Exception as e:
        print(f"Error during sending telegram message: {e}")


@shared_task
def send_notify_overdue():
    """Task to send Telegram message, if taken boom exceeded due date"""

    # due_date_books_list = BookDetail.objects.filter(is_overdue=False)
    due_date_books_list = BookDetail.objects.filter(is_overdue=False)

    local_current_date_time = localtime(timezone.now()).date()  # Get local current time

    for book in due_date_books_list:
        if book.due_date:
            one_day_time = timedelta(days=1)
            current_difference = local_current_date_time - book.due_date.date()

            # If day exceeds due date on one day, then Overdue status turns ti True and message is sending to the user
            if current_difference == one_day_time:

                book.is_overdue = True
                book.save()
                fee = 0
                client_tg_chat_id = book.client.telegram_chat_id
                if str(book.feature) == "Rare":
                    fee = RARE_FEE
                elif str(book.feature) == "Expensive":
                    fee = EXPENSIVE_FEE
                elif str(book.feature) == "No_features":
                    fee = NO_FEATURES_FEE

                day_fee = book.book_finance.price * fee

                # Specifying daily  message
                message_fee = f"Daily fee is {day_fee}"

                # General message
                message = (
                    f'You have overdue for a book "{book}", author: {book.book_general.author}. Please, return soon as possible. '
                    + message_fee
                )

                try:
                    send_telegram_message(client_tg_chat_id, message)
                except Exception as e:
                    print(f"Error during sending telegram message: {e}")


@shared_task
def send_reminder_soon_overdue():
    """Task to send Telegram message, for 3 days before overdue and one day before overdue"""

    local_current_date_time = localtime(timezone.now()).date()  # Get local current time

    # Get list of the books, which are taken by Clients and defining unique user
    clients_with_books = (
        BookDetail.objects.values_list("client_id").exclude(client_id=None).distinct()
    )

    for client in clients_with_books:

        # Get client's ID
        client_id = client[0]

        # Check if particular client books without Overdue
        book_exists = BookDetail.objects.filter(
            client_id=client_id, is_overdue=False
        ).exists()

        if book_exists:

            # Gets particular book, which is on hand at particular client
            books = BookDetail.objects.filter(client_id=client_id, is_overdue=False)
            for book in books:

                # Gets TG Chat id for particular user
                client_tg_chat_id = book.client.telegram_chat_id

                due_date = book.due_date.date()
                three_days_time = timedelta(days=3)

                one_day_time = timedelta(days=1)

                # Gets current difference in days between today and due date
                current_difference = due_date - local_current_date_time

                message = ""

                # Sets logic for notification before 3 days for expiring
                if current_difference == three_days_time:
                    message = f'You have overdue for a book "{book}", author: {book.book_general.author} in 3 days'

                # Sets logic for notification before 1 day for expiring
                if current_difference == one_day_time:
                    message = f'You have overdue for a book "{book}", author: {book.book_general.author} in 1 day'

                try:
                    send_telegram_message(client_tg_chat_id, message)
                except Exception as e:
                    print(f"Error during sending telegram message: {e}")


@shared_task
def calculate_overdue_penalty():
    """Task to calculate overdue fees"""

    local_current_date_time = localtime(timezone.now()).date()  # Get local current time

    # Check if overdue books exist
    overdue_books_exist = BookDetail.objects.filter(is_overdue=True).exists
    if overdue_books_exist:

        # Gets a list of Books in overdue
        overdue_books = BookDetail.objects.filter(is_overdue=True)
        fee = 0

        # Defines feature of the book and sets fee on this basis
        for book in overdue_books:
            if str(book.feature) == "Rare":
                fee = RARE_FEE
            elif str(book.feature) == "Expensive":
                fee = EXPENSIVE_FEE
            elif str(book.feature) == "No_features":
                fee = NO_FEATURES_FEE

            day_fee = book.book_finance.price * fee

            # Sets a logic to count overdue dates, accumulated fees
            book.book_finance.overdue_day += 1
            if not book.book_finance.overdue_date:
                book.book_finance.overdue_date = local_current_date_time
            book.book_finance.penalty_sum += day_fee
            book.book_finance.save()
