import datetime
from datetime import timedelta

from celery import shared_task
from django.utils import timezone
from django.utils.timezone import localtime

from books.models import Habit
from books.services import send_telegram_message


@shared_task
def send_reminder_and_set_next_date():
    """Task to send Telegram message, if user chose option to get telegram messages"""
    useful_habits_list = Habit.objects.filter(
        is_nice_habit=False
    )  # Get all books which fo not have parameter Nice Habit
    local_current_date_time = localtime(timezone.now())  # Get local current time

    for habit in useful_habits_list:
        local_habit_date = localtime(
            habit.habit_date
        )  # Get Habit time in local Timezone
        next_habit_time = local_habit_date + timedelta(
            days=habit.habit_period
        )  # Set Next time for chosen Habit

        # If user has Telegram ID
        if habit.habit_user.telegram_chat_id:
            formatted_habit_date = local_habit_date.strftime("%Y-%m-%d %H:%M")
            formatted_next_habit_time = next_habit_time.strftime("%Y-%m-%d %H:%M")

            # Set different messages, depends on if Habit does have related habit or reward
            reward_message = f"\nYou also deserved {habit.habit_reward}"
            related_habit_message = (
                f"\nDo not forget about nice habit {habit.related_habit}"
            )
            message = (
                f"Hello, "
                f'dear {habit.habit_user.first_name if habit.habit_user.first_name else "User"},'
                f'soon time for your habit - "{habit.habit_action}"'
                f"It starts at {formatted_habit_date}."
                f"\nTime duration is {habit.habit_time_duration} seconds."
                f"Place is {habit.habit_place}.\n"
                f'\nNext time for a habit "{habit.habit_name}" '
                f"will occur in {habit.habit_period} days: {formatted_next_habit_time} "
                f"at {habit.habit_place}.\n"
            )

            if habit.habit_reward:
                final_message = message + reward_message
            elif habit.related_habit:
                final_message = message + related_habit_message
            else:
                final_message = message

            # Set notification time one hour before schedule habit
            alarm_time = local_habit_date - datetime.timedelta(minutes=60)

            # Alarm comes before time for scheduled habit and actual alarm time
            if alarm_time <= local_current_date_time <= local_habit_date:
                try:
                    send_telegram_message(
                        habit.habit_user.telegram_chat_id, final_message
                    )

                except Exception as e:
                    print(f"Ошибка при отправке сообщения: {e}")

        # Sets next Schedule date and time after passing Habit date/time curent schedule
        if local_current_date_time >= local_habit_date:
            habit.habit_date = local_habit_date + timedelta(days=habit.habit_period)
            habit.save()
