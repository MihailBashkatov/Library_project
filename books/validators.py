from datetime import timedelta

from rest_framework.serializers import ValidationError
from django.utils import timezone
from django.utils.timezone import localtime
from books.models import BookDetail, BookGeneral
# from books.serializers import BookDetailSerializer


# from books.serializers import BookDetailSerializer


class IsBookTaken:
    """
    Adding validator to check if client who has a book exists,
    then not possible to assign another client until client value  set for Null"""

    requires_context = True

    def __init__(self, field):
        self.field = field

    def __call__(self, value, serializer):
        # book = serializer.instance.book_volume.all()[0].page_amount
        # print(book)
        book = serializer.instance
        book_id = (str(serializer.context.get("request").path).split('update/')[-1].strip('/'))
        client = value.get("client")
        if BookDetail.objects.get(id=book_id).client:
            if client:
                current_client = BookDetail.objects.filter(client=client, id=book_id).exists()

                if not current_client:
                    raise ValidationError(f"book is already taken by client {client.email}. "
                                          f"Books need to be return before assigning for a new client")
                book.taken_by_client = localtime(timezone.now()) # Get local current time
                book.due_date = book.taken_by_client + timedelta(days=30) # Set time for returning the book
                book.save()

        if client is not None:
            book.taken_by_client = localtime(timezone.now())  # Get local current time
            book.due_date = book.taken_by_client + timedelta(days=30)  # Set time for returning the book
            book.save()
        else:
            book.taken_by_client = None # Set null
            book.due_date = None  # Set null
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
