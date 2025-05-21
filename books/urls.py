from django.urls import path

from books.apps import BooksConfig
from books.views import (AuthorCreateAPIView, AuthorDestroyAPIView,
                         AuthorRetrieveAPIView, AuthorsListAPIView,
                         AuthorUpdateAPIView, BookCreateAPIView,
                         BookDestroyAPIView, BookFinanceCreateAPIView,
                         BookFinanceDestroyAPIView, BookFinanceRetrieveAPIView,
                         BookFinancesListAPIView, BookFinanceUpdateAPIView,
                         BookGeneralCreateAPIView, BookGeneralDestroyAPIView,
                         BookGeneralRetrieveAPIView, BookGeneralsListAPIView,
                         BookGeneralUpdateAPIView, BookRetrieveAPIView,
                         BooksListAPIView, BooksUserListAPIView,
                         BookUpdateAPIView, GenreCreateAPIView,
                         GenreDestroyAPIView, GenreRetrieveAPIView,
                         GenresListAPIView, GenreUpdateAPIView,
                         LibrariesListAPIView, LibraryCreateAPIView,
                         LibraryDestroyAPIView, LibraryRetrieveAPIView,
                         LibraryUpdateAPIView)

app_name = BooksConfig.name


urlpatterns = [
    # Paths for Book CRUD
    path("book/create/", BookCreateAPIView.as_view(), name="book-create"),
    path("books/", BooksListAPIView.as_view(), name="books-list"),
    path("book/<int:pk>/", BookRetrieveAPIView.as_view(), name="book-detail"),
    path("book/update/<int:pk>/", BookUpdateAPIView.as_view(), name="book-update"),
    path("book/delete/<int:pk>/", BookDestroyAPIView.as_view(), name="book-delete"),
    # Path to get only users list of books
    path("user/books/", BooksUserListAPIView.as_view(), name="books-user-list"),
    # Paths for Author CRUD
    path("author/create/", AuthorCreateAPIView.as_view(), name="author-create"),
    path("authors/", AuthorsListAPIView.as_view(), name="authors-list"),
    path("author/<int:pk>/", AuthorRetrieveAPIView.as_view(), name="author-detail"),
    path(
        "author/update/<int:pk>/", AuthorUpdateAPIView.as_view(), name="author-update"
    ),
    path(
        "author/delete/<int:pk>/", AuthorDestroyAPIView.as_view(), name="author-delete"
    ),
    # Paths for Book General Description CRUD
    path(
        "book_general/create/",
        BookGeneralCreateAPIView.as_view(),
        name="book_general-create",
    ),
    path(
        "books_general/", BookGeneralsListAPIView.as_view(), name="book_generals-list"
    ),
    path(
        "book_general/<int:pk>/",
        BookGeneralRetrieveAPIView.as_view(),
        name="book_general-detail",
    ),
    path(
        "book_general/update/<int:pk>/",
        BookGeneralUpdateAPIView.as_view(),
        name="book_general-update",
    ),
    path(
        "book_general/delete/<int:pk>/",
        BookGeneralDestroyAPIView.as_view(),
        name="book_general-delete",
    ),
    # Paths for Library CRUD
    path("library/create/", LibraryCreateAPIView.as_view(), name="library-create"),
    path("libraries/", LibrariesListAPIView.as_view(), name="libraries-list"),
    path("library/<int:pk>/", LibraryRetrieveAPIView.as_view(), name="library-detail"),
    path(
        "library/update/<int:pk>/",
        LibraryUpdateAPIView.as_view(),
        name="library-update",
    ),
    path(
        "library/delete/<int:pk>/",
        LibraryDestroyAPIView.as_view(),
        name="library-delete",
    ),
    # Paths for Genre CRUD
    path("genre/create/", GenreCreateAPIView.as_view(), name="genre-create"),
    path("genres/", GenresListAPIView.as_view(), name="genres-list"),
    path("genre/<int:pk>/", GenreRetrieveAPIView.as_view(), name="genre-detail"),
    path("genre/update/<int:pk>/", GenreUpdateAPIView.as_view(), name="genre-update"),
    path("genre/delete/<int:pk>/", GenreDestroyAPIView.as_view(), name="genre-delete"),
    # Paths for BookFinance CRUD
    path(
        "book_finance/create/",
        BookFinanceCreateAPIView.as_view(),
        name="book_finance-create",
    ),
    path(
        "book_finances/", BookFinancesListAPIView.as_view(), name="book_finances-list"
    ),
    path(
        "book_finance/<int:pk>/",
        BookFinanceRetrieveAPIView.as_view(),
        name="book_finance-detail",
    ),
    path(
        "book_finance/update/<int:pk>/",
        BookFinanceUpdateAPIView.as_view(),
        name="book_finance-update",
    ),
    path(
        "book_finance/delete/<int:pk>/",
        BookFinanceDestroyAPIView.as_view(),
        name="book_finance-delete",
    ),
    # path("habit/public/<int:pk>/", PublicAPIView.as_view(), name="public-habit"),
]
