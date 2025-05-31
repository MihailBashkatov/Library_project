from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import (Author, BookDetail, BookFeature,
                          BookFinance, BookGeneral, BookGenre, Library)
from users.models import User


class LibraryTestCase(APITestCase):

    def setUp(self) -> None:
        self.user_1 = User.objects.create(email="user1@user.com")
        self.user_1.is_staff = True
        self.user_1.save()
        self.library = Library.objects.create(
            name="Library", main_page="Main page text", rules_page="Rules page text"
        )

        self.client.force_authenticate(user=self.user_1)

    def test_library_retrieve(self):
        url = reverse("books:library-detail", args=(self.library.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Library")
        self.assertEqual(data.get("main_page"), "Main page text")
        self.assertEqual(data.get("rules_page"), "Rules page text")

    def test_library_create(self):
        url = reverse("books:library-create")

        data = {
            "name": "Library_2",
            "main_page": "Main page text 2",
            "rules_page": "Rules page text 2",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Library.objects.all().count(), 2)
        self.assertEqual(
            response.json(),
            {
                "id": self.library.pk + 1,
                "name": "Library_2",
                "main_page": "Main page text 2",
                "rules_page": "Rules page text 2",
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
            name="Lev", surname="Tolstoy", birth_date="1828-10-28"
        )

        self.client.force_authenticate(user=self.user_1)

    def test_author_retrieve(self):
        url = reverse("books:author-detail", args=(self.author.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Lev")
        self.assertEqual(data.get("surname"), "Tolstoy")
        self.assertEqual(data.get("birth_date"), "1828-10-28")

    def test_author_create(self):
        url = reverse("books:author-create")

        data = {"name": "Ivane", "surname": "Ivanov", "birth_date": "2000-04-20"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Author.objects.all().count(), 2)
        self.assertEqual(
            response.json(),
            {"name": "Ivane", "surname": "Ivanov", "birth_date": "2000-04-20"},
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
            feature="No_features",
        )

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
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(BookFeature.objects.all().count(), 2)
        self.assertEqual(
            response.json(),
            {
                "id": self.feature.pk + 1,
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
                    "id": self.feature.pk,
                },
            ],
        }

        self.assertEqual(BookFeature.objects.all().count(), 1)
        self.assertEqual(data, result)


class BookDetailTestCase(APITestCase):

    def setUp(self) -> None:
        self.user_1 = User.objects.create(email="user1@user.com")
        self.user_1.is_librarian = True
        self.user_1.save()

        self.library = Library.objects.create(
            name="Library", main_page="Main page text", rules_page="Rules page text"
        )

        self.author = Author.objects.create(
            name="Lev", surname="Tolstoy", birth_date="1828-10-28"
        )

        self.feature = BookFeature.objects.create(feature="No_features")

        self.genre = BookGenre.objects.create(genre="Kids")

        self.book_general = BookGeneral.objects.create(
            library=self.library,
            title="Маленький принц",
            author=self.author,
            description="Description of the General book",
            age_restriction=0,
            genre=self.genre,
        )

        self.book = BookDetail.objects.create(
            book_general=self.book_general,
            edition_year="1983-08-25",
            page_amount=375,
            feature=self.feature,
            client=self.user_1,
        )

        self.client.force_authenticate(user=self.user_1)

    def test_book_retrieve(self):
        url = reverse("books:book-detail", args=(self.book.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("page_amount"), 375)
        self.assertEqual(data.get("book_general").get("title"), "Маленький принц")
        self.assertEqual(data.get("feature"), self.feature.pk)

    def test_book_create(self):
        url = reverse("books:book-create")

        data = {
            "book_general": self.book_general.pk,
            "edition_year": "2020-12-20",
            "page_amount": 100,
            "feature": self.feature.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(BookDetail.objects.all().count(), 2)

    def test_book_update(self):
        url = reverse("books:book-update", args=(self.book.pk,))
        data = {
            "book_general": self.book_general.pk,
            "page_amount": 300,
            "edition_year": "1998-01-03",
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("page_amount"), 300)
        self.assertEqual(data.get("edition_year"), "1998-01-03")

    def test_book_delete(self):
        url = reverse("books:book-delete", args=(self.book.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BookDetail.objects.all().count(), 0)

    def test_books_list(self):
        url = reverse("books:books-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.book.pk,
                    "book_general": {
                        "id": self.book_general.pk,
                        "library": self.book_general.library.pk,
                        "title": self.book_general.title,
                        "author": self.book_general.author.pk,
                        "description": self.book_general.description,
                        "age_restriction": self.book_general.age_restriction,
                        "rating": self.book_general.rating,
                        "is_available": self.book_general.is_available,
                        "genre": {"genre": self.genre.genre},
                        "is_book_popular": self.book_general.is_book_popular,
                    },
                    "client": {
                        "id": self.user_1.id,
                        "email": self.user_1.email,
                        "password": self.user_1.password,
                        "telegram_chat_id": self.user_1.telegram_chat_id,
                    },
                    "edition_year": self.book.edition_year,
                    "page_amount": self.book.page_amount,
                    "taken_by_client": None,
                    "due_date": None,
                    "is_overdue": False,
                    "picture": None,
                    "book_content": [],
                    "feature": self.feature.pk,
                    "book_finance": None,
                    "book_volume": [],
                }
            ],
        }

        self.assertEqual(BookDetail.objects.all().count(), 1)
        self.assertEqual(data, result)


class BookGeneralTestCase(APITestCase):

    def setUp(self) -> None:
        self.user_1 = User.objects.create(email="user1@user.com")
        self.user_1.is_librarian = True
        self.user_1.save()

        self.library = Library.objects.create(
            name="Library", main_page="Main page text", rules_page="Rules page text"
        )

        self.author = Author.objects.create(
            name="Lev", surname="Tolstoy", birth_date="1828-10-28"
        )

        self.genre = BookGenre.objects.create(genre="Kids")

        self.book_general = BookGeneral.objects.create(
            library=self.library,
            title="Маленький принц",
            author=self.author,
            description="Description of the General book",
            age_restriction=0,
            genre=self.genre,
        )

        self.client.force_authenticate(user=self.user_1)

    def test_book_general_retrieve(self):
        url = reverse("books:book_general-detail", args=(self.book_general.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Маленький принц")
        self.assertEqual(data.get("library"), self.library.pk)
        self.assertEqual(data.get("author"), self.author.pk)

    def test_book_delete(self):
        url = reverse("books:book_general-delete", args=(self.book_general.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BookFeature.objects.all().count(), 0)

    def test_books_general_list(self):
        url = reverse("books:book_generals-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.book_general.pk,
                    "library": self.library.pk,
                    "title": self.book_general.title,
                    "author": self.author.pk,
                    "description": self.book_general.description,
                    "age_restriction": self.book_general.age_restriction,
                    "rating": self.book_general.rating,
                    "is_available": self.book_general.is_available,
                    "genre": {"genre": self.genre.genre},
                    "is_book_popular": self.book_general.is_book_popular,
                }
            ],
        }

        self.assertEqual(BookGeneral.objects.all().count(), 1)
        self.assertEqual(data, result)


class BookGenreTestCase(APITestCase):

    def setUp(self) -> None:
        self.user_1 = User.objects.create(email="user1@user.com")
        self.user_1.is_librarian = True
        self.user_1.save()

        self.genre = BookGenre.objects.create(genre="Kids")

        self.client.force_authenticate(user=self.user_1)

    def test_genre_retrieve(self):
        url = reverse("books:genre-detail", args=(self.genre.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("genre"), "Kids")

    def test_genre_create(self):
        url = reverse("books:genre-create")

        data = {"genre": "Horror"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(BookGenre.objects.all().count(), 2)
        self.assertEqual(response.json(), {"genre": "Horror"})

    def test_genre_update(self):
        url = reverse("books:genre-update", args=(self.genre.pk,))
        data = {"genre": "Fantasy"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("genre"), "Fantasy")

    def test_genre_delete(self):
        url = reverse("books:genre-delete", args=(self.genre.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BookFeature.objects.all().count(), 0)

    def test_genres_list(self):
        url = reverse("books:genres-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [{"genre": self.genre.genre}],
        }

        self.assertEqual(BookGenre.objects.all().count(), 1)
        self.assertEqual(data, result)


class BookFinanceTestCase(APITestCase):

    def setUp(self) -> None:
        self.user_1 = User.objects.create(email="user1@user.com")
        self.user_1.is_staff = True
        self.user_1.save()

        self.library = Library.objects.create(
            name="Library", main_page="Main page text", rules_page="Rules page text"
        )

        self.author = Author.objects.create(
            name="Lev", surname="Tolstoy", birth_date="1828-10-28"
        )

        self.feature = BookFeature.objects.create(feature="No_features")

        self.genre = BookGenre.objects.create(genre="Kids")

        self.book_general = BookGeneral.objects.create(
            library=self.library,
            title="Маленький принц",
            author=self.author,
            description="Description of the General book",
            age_restriction=0,
            genre=self.genre,
        )

        self.book = BookDetail.objects.create(
            book_general=self.book_general,
            edition_year="1983-08-25",
            page_amount=375,
            feature=self.feature,
            client=self.user_1,
        )

        self.book_1 = BookDetail.objects.create(
            book_general=self.book_general,
            edition_year="1983-08-25",
            page_amount=375,
            feature=self.feature,
            client=self.user_1,
        )

        self.book_finance = BookFinance.objects.create(book=self.book, price=100)

        self.client.force_authenticate(user=self.user_1)

    def test_book_finance_retrieve(self):
        url = reverse("books:book_finance-detail", args=(self.book_finance.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("price"), 100)
        self.assertEqual(data.get("book"), self.book.pk)

    def test_book_finance_create(self):
        url = reverse("books:book_finance-create")

        data = {
            "book": self.book_1.pk,
            "price": 200.0,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(BookFinance.objects.all().count(), 2)

    def test_book_finance_update(self):
        url = reverse("books:book_finance-update", args=(self.book_finance.pk,))
        data = {"book": self.book.pk, "price": 200.00}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("price"), 200.00)

    def test_book_finance_delete(self):
        url = reverse("books:book_finance-delete", args=(self.book_finance.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BookFinance.objects.all().count(), 0)

    def test_books_finance_list(self):
        url = reverse("books:book_finances-list")
        response = self.client.get(url)
        data = response.json()

        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "book": self.book.pk,
                    "price": self.book_finance.price,
                    "overdue_day": self.book_finance.overdue_day,
                    "overdue_date": self.book_finance.overdue_date,
                    "penalty_sum": self.book_finance.penalty_sum,
                }
            ],
        }

        self.assertEqual(BookFinance.objects.all().count(), 1)
        self.assertEqual(data, result)


class BookDetailUserTestCase(APITestCase):

    def setUp(self) -> None:
        self.user_1 = User.objects.create(email="user1@user.com")
        self.user_1.save()

        self.library = Library.objects.create(
            name="Library", main_page="Main page text", rules_page="Rules page text"
        )

        self.author = Author.objects.create(
            name="Lev", surname="Tolstoy", birth_date="1828-10-28"
        )

        self.feature = BookFeature.objects.create(feature="No_features")

        self.genre = BookGenre.objects.create(genre="Kids")

        self.book_general = BookGeneral.objects.create(
            library=self.library,
            title="Маленький принц",
            author=self.author,
            description="Description of the General book",
            age_restriction=0,
            genre=self.genre,
        )

        self.book = BookDetail.objects.create(
            book_general=self.book_general,
            edition_year="1983-08-25",
            page_amount=375,
            feature=self.feature,
            client=self.user_1,
        )

        self.client.force_authenticate(user=self.user_1)

    def test_book_retrieve(self):
        url = reverse("books:book_user-detail", args=(self.book.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("page_amount"), 375)
        self.assertEqual(data.get("book_general").get("title"), "Маленький принц")
        self.assertEqual(data.get("feature"), self.feature.pk)

    def test_books_list(self):
        url = reverse("books:books-user-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.book.pk,
                    "book_general": {
                        "id": self.book_general.pk,
                        "library": self.book_general.library.pk,
                        "title": self.book_general.title,
                        "author": self.book_general.author.pk,
                        "description": self.book_general.description,
                        "age_restriction": self.book_general.age_restriction,
                        "rating": self.book_general.rating,
                        "is_available": self.book_general.is_available,
                        "genre": {"genre": self.genre.genre},
                        "is_book_popular": self.book_general.is_book_popular,
                    },
                    "client": {
                        "id": self.user_1.id,
                        "email": self.user_1.email,
                        "password": self.user_1.password,
                        "telegram_chat_id": self.user_1.telegram_chat_id,
                    },
                    "edition_year": self.book.edition_year,
                    "page_amount": self.book.page_amount,
                    "taken_by_client": None,
                    "due_date": None,
                    "is_overdue": False,
                    "picture": None,
                    "book_content": [],
                    "feature": self.feature.pk,
                    "book_finance": None,
                    "book_volume": [],
                }
            ],
        }

        self.assertEqual(BookDetail.objects.all().count(), 1)
        self.assertEqual(data, result)


# class BookUpdateClientTestCase(APITestCase):
#
#     def setUp(self) -> None:
#         self.user_1 = User.objects.create(email="user1@user.com")
#         self.user_1.is_librarian = True
#         self.user_1.save()
#
#         self.user_2 = User.objects.create(email="user2@user.com")
#
#         self.library = Library.objects.create(
#             name="Library", main_page="Main page text", rules_page="Rules page text"
#         )
#
#         self.author = Author.objects.create(
#             name="Lev", surname="Tolstoy", birth_date="1828-10-28"
#         )
#
#         self.feature = BookFeature.objects.create(feature="No_features")
#
#         self.genre = BookGenre.objects.create(genre="Kids")
#
#         self.book_general = BookGeneral.objects.create(
#             library=self.library,
#             title="Маленький принц",
#             author=self.author,
#             description="Description of the General book",
#             age_restriction=0,
#             genre=self.genre,
#         )
#
#         self.book = BookDetail.objects.create(
#             book_general=self.book_general,
#             edition_year="1983-08-25",
#             page_amount=375,
#             feature=self.feature,
#         )
#
#         self.archive = Archive.objects.create()
#
#         self.client.force_authenticate(user=self.user_1)
#
#     def test_book_client_update(self):
#         url = reverse("books:book_client-update", args=(self.book.pk,))
#         data = {"client": self.user_2.pk}
#         response = self.client.patch(url, data)
#
#         data = response.json()
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(data.get("client"), self.user_2.pk)