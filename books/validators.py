from datetime import timedelta

from rest_framework.serializers import ValidationError
from django.utils import timezone
from django.utils.timezone import localtime
from books.models import BookDetail, BookGeneral, Archive


# from books.serializers import BookDetailSerializer


# from books.serializers import BookDetailSerializer


class IsBookTaken:
    """
    Adding validator to check if client, who has a book ,exists,
    then not possible to assign another client until client value set for Null
    Also there is a logic to set new order in tha tbale Archive and steps in case client wants to prolong
    ordered book"""

    requires_context = True

    def __init__(self, field):
        self.field = field

    def __call__(self, value, serializer):

        # Get BookDetailClientSerializer
        book = serializer.instance

        # Get BookDetail ID
        book_id = (str(serializer.context.get("request").path).split('update/')[-1].strip('/'))

        # Get client
        client = value.get("client")

        # If client exists, get client's user_card
        if client:
            user_card = client.user_card

        # Set local time
        time_now = localtime(timezone.now())

        # Get ArchiveOrderSerializer from instance
        archived_order = serializer.instance.archive_order

        # Logic if client is chosen as None. It is needed when client returns a book and then
        # book is not linked to any client, taken time and due date are becoming Null
        if not client:
            book.taken_by_client = None  # Set null
            book.due_date = None  # Set null
            book.client = None # Set null
            book.save()

            # Logic to find if order for the book exists. If exists, then in Archive table this order sets time
            # of the book return. In case order does not exist, nothing happen

            search_order = archived_order.filter(title=book, return_date=None).exists()
            if search_order:
                order = archived_order.get(title=book, return_date=None)
                order.return_date = time_now
                order.save()
            else:
                pass

        # Logic if any client is already having book (ordered it earlier). It is needed when client wants to
        # prolong the order. If another client will try to book this book, it will not be allowed
        elif BookDetail.objects.get(id=book_id).client:
            if client:
                current_client = BookDetail.objects.filter(client=client, id=book_id).exists()

                # Check if targeted client is a client, who already has a book
                if not current_client:
                    raise ValidationError(f"book is already taken by client {client.email}. "
                                          f"Books need to be return before assigning for a new client")

                # Search the book, which is on hand at current client
                search_order = archived_order.filter(title=book, return_date=None).exists
                if search_order:
                    order = archived_order.get(title=book, return_date=None)

                    # Checks how many times order was prolonged. Maximum is 2 times
                    if order.order_continued_times == 2:
                        raise ValidationError(f"Book order is already renewed 2 times. No possibility to renew more")
                    order.order_continued_times += 1
                    order.save()

                    # Sets new time of order in the table BookDetail and new due date
                    book.taken_by_client = time_now  # Get local current time
                    book.due_date = book.taken_by_client + timedelta(days=30)  # Set time for returning the book
                    book.save()


        else:

            # For new order, sets time in the table BookDetail
            book.taken_by_client = time_now  # Get local current time

            # Adding new order to table Archive
            archived_order.create(title=book, user_card=user_card, taken_by_client=time_now)

            # Sets due date time in the table BookDetail
            book.due_date = book.taken_by_client + timedelta(days=30)  # Set time for returning the book
            book.save()




# class HabitPeriodValidator:
#     """
#     Adding validator to check if repetitive period between books shall not be more than 7 days
#     """
#
#     def __init__(self, field):
#         self.field = field
#
#     def __call__(self, value):
#         habit_period = value.get("habit_period")
#         if habit_period:
#             if habit_period > 7:
#                 raise ValidationError(
#                     "Time period between repeats books shall not be more then 7 days"
#                 )
#             if habit_period == 0:
#                 raise ValidationError(
#                     "Time period between repeats books shall not be 0 days"
#                 )
#
#
# class RewardOrHabitRelatedValidator:
#     """
#     Adding validator to check if Related habit does not appear together with Reward"""
#
#     requires_context = True
#
#     def __init__(self, field):
#         self.field = field
#
#     def __call__(self, value, serializer):
#         if not serializer.instance:
#             if value.get("related_habit") and value.get("habit_reward"):
#                 raise ValidationError(
#                     "You can choose either Reward or Related Habit, but not both at once."
#                 )
#         else:
#             if serializer.instance.related_habit and value.get("habit_reward"):
#                 raise ValidationError(
#                     f"You can choose either Reward or Related Habit, but not both at once."
#                     f" Currently you have Related Habit: {serializer.instance.related_habit}"
#                 )
#             if serializer.instance.habit_reward and value.get("related_habit"):
#                 raise ValidationError(
#                     f"You can choose either Reward or Related Habit, but not both at once."
#                     f" Currently you have Reward: {serializer.instance.habit_reward}"
#                 )
#
#
# class NiceHabitRelatedValidator:
#     """
#     Adding validator to check if Related habit is Nice Habit"""
#
#     def __init__(self, field):
#         self.field = field
#
#     def __call__(self, value):
#         if value.get("related_habit") and not value.get("related_habit").is_nice_habit:
#
#             raise ValidationError(
#                 f"You can choose Related Habit only if it is Nice Habit. "
#                 f"Currently {value.get('related_habit').habit_name} is not Nice Habit"
#             )
#
#
# class NiceNotRewardNotRelatedHabitValidator:
#     """
#     Adding validator to check if Nice habit can't have Related Habit or Reward"""
#
#     requires_context = True
#
#     def __init__(self, field):
#         self.field = field
#
#     def __call__(self, value, serializer):
#
#         if value.get("is_nice_habit") and (
#             serializer.instance.habit_reward or serializer.instance.related_habit
#         ):
#
#             raise ValidationError(
#                 "You can't have Nice Habit if Related habit or Reward is in place."
#             )
