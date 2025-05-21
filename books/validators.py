from rest_framework.serializers import ValidationError


class IsVolumeExist:
    """
    Adding validator to check if volume exists, then number of pages van be null"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        book_volume = value.get("book_volume")
        if len(book_volume) == 0:
            # if time_duration > 120:
            raise ValidationError("Time duration shall not be more than 120 seconds")


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
