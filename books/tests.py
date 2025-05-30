from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Library, Author, BookFeature
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


    def test_library_create(self):
        url = reverse("books:library-create")

        data = {
            "name": "Library_2",
            "main_page": "Main page text 2",
            "rules_page": "Rules page text 2"
        }
        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Library.objects.all().count(), 2)
        self.assertEqual(
            response.json(),
            {
                "id": 2,
                "name":"Library_2",
                "main_page": "Main page text 2",
                "rules_page": "Rules page text 2"
            },
        )
    #
    def test_library_update(self):
        url = reverse("books:library-update", args=(self.library.pk,))
        data = {"name": "Library_3"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Library_3")

    def test_library_delete(self):
        url = reverse("books:library-delete", args=(self.library.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Library.objects.all().count(), 0)

    def test_library_list(self):
        url = reverse("books:libraries-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "name": self.library.name,
                    "main_page": self.library.main_page,
                    "rules_page": self.library.rules_page,
                    "id": self.library.id,
                }
            ],
        }

        self.assertEqual(Library.objects.all().count(), 1)
        self.assertEqual(data, result)

class AuthorTestCase(APITestCase):

    def setUp(self) -> None:
        self.user_1 = User.objects.create(email="user1@user.com")
        self.user_1.is_librarian = True
        self.user_1.save()
        self.author = Author.objects.create(
            name="Lev",
            surname='Tolstoy',
            birth_date='1828-10-28')

        self.client.force_authenticate(user=self.user_1)

    def test_author_retrieve(self):
        url = reverse("books:author-detail", args=(self.author.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Lev")
        self.assertEqual(data.get("surname"), 'Tolstoy')
        self.assertEqual(data.get("birth_date"), '1828-10-28')

    def test_author_create(self):
        url = reverse("books:author-create")

        data = {
            "name": "Ivane",
            "surname": "Ivanov",
            "birth_date": "2000-04-20"
        }
        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Author.objects.all().count(), 2)
        self.assertEqual(
                response.json(),
                {
                "name": "Ivane",
                "surname": "Ivanov",
                "birth_date": "2000-04-20"
            },
        )

        #
    def test_author_update(self):
        url = reverse("books:author-update", args=(self.author.pk,))
        data = {"name": "Semen"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Semen")

    def test_author_delete(self):
        url = reverse("books:author-delete", args=(self.author.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.all().count(), 0)

    def test_author_list(self):
        url = reverse("books:authors-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                "name": self.author.name,
                "surname": self.author.surname,
                "birth_date": self.author.birth_date,

                }
            ],
        }

        self.assertEqual(Author.objects.all().count(), 1)
        self.assertEqual(data, result)

class BookFeatureTestCase(APITestCase):

    def setUp(self) -> None:
        self.user_1 = User.objects.create(email="user1@user.com")
        self.user_1.is_staff = True
        self.user_1.save()
        self.feature = BookFeature.objects.create(
            feature="No_features", )

        self.client.force_authenticate(user=self.user_1)

    def test_feature_retrieve(self):
        url = reverse("books:feature-detail", args=(self.feature.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("feature"), "No_features")

    def test_feature_create(self):
        url = reverse("books:feature-create")

        data = {
            "feature": "Expensive",
        }
        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(BookFeature.objects.all().count(), 2)
        self.assertEqual(
        response.json(),
        {
                "id": 2,
                "feature": "Expensive",
            },
        )

    def test_feature_update(self):
        url = reverse("books:feature-update", args=(self.feature.pk,))
        data = {"feature": "Rare"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("feature"), "Rare")

    def test_feature_delete(self):
        url = reverse("books:feature-delete", args=(self.feature.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BookFeature.objects.all().count(), 0)

    def test_feature_list(self):
        url = reverse("books:features-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {

                    "feature": "No_features",
                    "id": 4,
                },
            ]
        }

        self.assertEqual(BookFeature.objects.all().count(), 1)
        self.assertEqual(data, result)


    # def test_habit_public_available(self):
    #     url = reverse("books:public-habit", args=(self.habit.pk,))
    #     response = self.client.post(url)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Habit.objects.get(id=self.habit.pk).habit_is_public, False)
