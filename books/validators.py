from datetime import timedelta
from rest_framework.serializers import ValidationError
from django.utils import timezone
from django.utils.timezone import localtime
from books.models import BookDetail, Archive
from books.tasks import send_tg_message_book_taken, send_tg_message_book_returned, send_tg_message_book_renewed


class IsBookTaken:
    """
    Adding validator to check if client, who has a book ,exists,
    then not possible to assign another client until client value set for Null
    Also there is a logic to set new order in tha table Archive and steps in case client wants to prolong
    ordered book"""

    requires_context = True

    def __init__(self, field):
        self.field = field

    def __call__(self, value, serializer):

        # Get BookDetailClientSerializer
        book = serializer.instance

        # Get BookDetail ID
        book_id = (
            str(serializer.context.get("request").path).split("update/")[-1].strip("/")
        )

        # Get client
        client = value.get("client")


        # If client exists, get client's user_card
        if client:
            user_card = client.user_card

        # Set local time
        time_now = localtime(timezone.now())

        # Logic if client is chosen as None. It is needed when client returns a book and then
        # book is not linked to any client, taken time and due date are becoming Null

        # If book is returning
        if not client and book.client:

            # Get TG chat id of a client
            client_tg_chat_id = book.client.telegram_chat_id

            book.taken_by_client = None  # Set null
            book.due_date = None  # Set null
            book.client = None  # Set null


            # Send tg message to the client
            send_tg_message_book_returned.delay(client_tg_chat_id, str(book))
            book.save()

            # Logic to find if order for the book exists. If exists, then in Archive table this order sets time
            # of the book return. In case order does not exist, nothing happen

            search_order = Archive.objects.filter(title=book, return_date=None).exists()
            if search_order:
                order = Archive.objects.get(title=book, return_date=None)
                order.return_date = time_now
                order.save()
            else:
                pass

        # If no one  to return
        elif not client:
            book.taken_by_client = None  # Set null
            book.due_date = None  # Set null
            book.client = None  # Set null
            book.save()

            # Logic to find if order for the book exists. If exists, then in Archive table this order sets time
            # of the book return. In case order does not exist, nothing happen

            search_order = Archive.objects.filter(title=book, return_date=None).exists()
            if search_order:
                order = Archive.objects.get(title=book, return_date=None)
                order.return_date = time_now
                order.save()
            else:
                pass

        # Logic if any client is already having book (ordered it earlier). It is needed when client wants to
        # prolong the order. If another client will try to book this book, it will not be allowed
        elif BookDetail.objects.get(id=book_id).client:
            if client:
                current_client = BookDetail.objects.filter(
                    client=client, id=book_id
                ).exists()

                # Check if targeted client is a client, who already has a book
                if not current_client:
                    raise ValidationError(
                        f"book is already taken by client {BookDetail.objects.get(id=book_id).client}. "
                        f"Books need to be return before assigning for a new client"
                    )

                # Check if client who wants to prolog a book already has aa overdue
                client_overdue = BookDetail.objects.filter(
                    client=client, is_overdue=True
                ).exists()
                if client_overdue:
                    raise ValidationError(
                        f"Client {client} cannot prolong any book. Currently book "
                        f"{BookDetail.objects.get(client=client, is_overdue=True)} "
                        f"is in overdue"
                    )

                # Search the book, which is on hand at current client
                search_order = Archive.objects.filter(
                    title=book, return_date=None
                ).exists
                if search_order:
                    order = Archive.objects.get(title=book, return_date=None)

                    # Checks how many times order was prolonged. Maximum is 2 times
                    if order.order_continued_times == 2:
                        raise ValidationError(
                            f"Book order is already renewed 2 times. No possibility to renew more"
                        )
                    order.order_continued_times += 1
                    order.save()

                    # Sets new time of order in the table BookDetail and new due date
                    book.taken_by_client = time_now  # Get local current time

                    # Sets due date time in the table BookDetail
                    if str(book.feature) == 'Rare' or str(book.feature) == 'No_features':
                        book.due_date = book.taken_by_client + timedelta(
                            days=30
                        )

                    elif str(book.feature) == 'Expensive':
                        book.due_date = book.taken_by_client + timedelta(
                            days=15
                        )

                    # Get TG chat id of a client
                    client_tg_chat_id = client.telegram_chat_id

                    # Send tg message to the client
                    send_tg_message_book_renewed.delay(client_tg_chat_id, str(book), book.due_date)

                    book.save()

        else:

            books_name = Archive.objects.filter(
                user_card=client.user_card, return_date=None
            )

            # Check if client has more, than 4 books in hands
            if len(books_name) > 3:
                raise ValidationError(
                    f"Client {client} has more then 4 books. No possibility to take more"
                )

            # Check if client has overdue
            client_overdue = BookDetail.objects.filter(
                client=client, is_overdue=True
            ).exists()
            if client_overdue:
                raise ValidationError(
                    f"Client {client} cannot take any book. Currently book "
                    f"{BookDetail.objects.get(client=client, is_overdue=True)} "
                    f"is in overdue"
                )

            # For new order, sets time in the table BookDetail
            book.taken_by_client = time_now  # Get local current time

            # Adding new order to table Archive
            Archive.objects.create(
                title=book, user_card=user_card, taken_by_client=time_now
            )

            # Sets due date time in the table BookDetail
            if str(book.feature) == 'Rare' or str(book.feature) == 'No_features':
                book.due_date = book.taken_by_client + timedelta(
                    days=30
                )

            elif str(book.feature) == 'Expensive':
                book.due_date = book.taken_by_client + timedelta(
                    days=15
                )

            # Get TG chat id of a client
            client_tg_chat_id = client.telegram_chat_id

            # Send tg message to the client
            send_tg_message_book_taken.delay(client_tg_chat_id, str(book), book.due_date)


            book.save()
