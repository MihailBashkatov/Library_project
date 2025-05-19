from django.urls import path

from books.apps import BooksConfig
from books.views import BooksListAPIView, BookRetrieveAPIView, BookUpdateAPIView, BookDestroyAPIView

app_name = BooksConfig.name


urlpatterns = [
    # path("habit/create/", HabitCreateAPIView.as_view(), name="habit-create"),
    path("books/", BooksListAPIView.as_view(), name="books-list"),
    # path("user/books/", HabitsUserListAPIView.as_view(), name="books-user-list"),
    #
    path("book/<int:pk>/", BookRetrieveAPIView.as_view(), name="book-detail"),
    path(
        "book/update/<int:pk>/", BookUpdateAPIView.as_view(), name="book-update"
    ),
    path(
        "book/delete/<int:pk>/", BookDestroyAPIView.as_view(), name="book-delete"
    ),
    # path("habit/public/<int:pk>/", PublicAPIView.as_view(), name="public-habit"),

]
