from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Library
from users.models import User


class LibraryTestCase(APITestCase):

    def setUp(self) -> None:
        self.user_1 = User.objects.create(email="user1@user.com")
        self.user_1.is_staff = True
        self.user_1.save()
        self.library = Library.objects.create(
            name="Library",
            main_page='Main page text',
            rules_page='Rules page text')

        self.client.force_authenticate(user=self.user_1)

    def test_library_retrieve(self):
        url = reverse("books:library-detail", args=(self.library.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Library")
        self.assertEqual(data.get("main_page"), 'Main page text')
        self.assertEqual(data.get("rules_page"), 'Rules page text')

    # def test_habit_create(self):
    #     url = reverse("books:habit-create")
    #
    #     data = {
    #         "habit_name": "Jumping",
    #         "habit_user": self.user_1.id,
    #         "habit_place": "Street",
    #         "habit_action": "Jump",
    #         "habit_date": "2025-05-14 02:00",
    #         "habit_time_duration": 50,
    #         "related_habit": self.habit.id,
    #     }
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #
    #     self.assertEqual(Habit.objects.all().count(), 2)
    #     self.assertEqual(
    #         response.json(),
    #         {
    #             "id": 2,
    #             "habit_date": "2025-05-14T02:00:00+02:00",
    #             "habit_name": "Jumping",
    #             "habit_place": "Street",
    #             "habit_action": "Jump",
    #             "habit_time_duration": 50,
    #             "habit_is_public": False,
    #             "is_nice_habit": False,
    #             "habit_period": 1,
    #             "habit_reward": None,
    #             "habit_user": self.user_1.id,
    #             "related_habit": self.habit.id,
    #         },
    #     )
    #
    # def test_habit_update(self):
    #     url = reverse("books:habit-update", args=(self.habit.pk,))
    #     data = {"habit_name": "New Habit"}
    #     response = self.client.patch(url, data)
    #     data = response.json()
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(data.get("habit_name"), "New Habit")
    #
    # def test_habit_delete(self):
    #     url = reverse("books:habit-delete", args=(self.habit.pk,))
    #     response = self.client.delete(url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertEqual(Habit.objects.all().count(), 0)
    #
    # def test_habit_list(self):
    #     url = reverse("books:books-list")
    #     response = self.client.get(url)
    #     data = response.json()
    #     result = {
    #         "count": 1,
    #         "next": None,
    #         "previous": None,
    #         "results": [
    #             {
    #                 "habit_action": self.habit.habit_action,
    #                 "habit_date": "2025-05-11T15:00:00+02:00",
    #                 "habit_is_public": True,
    #                 "habit_name": self.habit.habit_name,
    #                 "habit_period": 1,
    #                 "habit_place": self.habit.habit_place,
    #                 "habit_reward": self.habit.habit_reward,
    #                 "habit_time_duration": self.habit.habit_time_duration,
    #                 "habit_user": self.habit.habit_user.id,
    #                 "id": self.habit.id,
    #                 "is_nice_habit": True,
    #                 "related_habit": None,
    #             }
    #         ],
    #     }
    #
    #     self.assertEqual(Habit.objects.all().count(), 1)
    #     self.assertEqual(data, result)
    #
    # def test_habit_public_available(self):
    #     url = reverse("books:public-habit", args=(self.habit.pk,))
    #     response = self.client.post(url)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Habit.objects.get(id=self.habit.pk).habit_is_public, False)
