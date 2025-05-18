from django.urls import path

from books.apps import BooksConfig

app_name = BooksConfig.name


# urlpatterns = [
#     path("habit/create/", HabitCreateAPIView.as_view(), name="habit-create"),
#     path("books/", HabitsListAPIView.as_view(), name="books-list"),
#     path("user/books/", HabitsUserListAPIView.as_view(), name="books-user-list"),
#
#     path("habit/<int:pk>/", HabitRetreiveAPIView.as_view(), name="habit-detail"),
#     path(
#         "habit/update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit-update"
#     ),
#     path(
#         "habit/delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit-delete"
#     ),
#     path("habit/public/<int:pk>/", PublicAPIView.as_view(), name="public-habit"),
#
# ]
