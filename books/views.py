# from django.http import HttpResponseForbidden
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError

from books.models import BookGeneral, BookDetail, Author, Library, BookGenre, BookFinance
from books.permissions import IsLibrarian, IsOwner, IsLibrarianAddBook
from books.serializers import BookGeneralSerializer, BookDetailSerializer, BookGenreSerializer, AuthorSerializer, \
    LibrarySerializer, BookFinanceSerializer

# from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from books.models import Habit
# from books.paginators import MyPagination
# from books.permissions import IsOwner
# from books.serializers import HabitSerializer
#
#
class BookCreateAPIView(generics.CreateAPIView):
    """View to create a book"""

    serializer_class = BookDetailSerializer
    permission_classes = [IsAuthenticated, IsLibrarianAddBook]

#
class BooksListAPIView(generics.ListAPIView):
    """View to create a list of public books"""

    serializer_class = BookDetailSerializer
    queryset = BookDetail.objects.all()
#
#     # access for all users
#     permission_classes = [
#         IsAuthenticated,
#     ]
#     pagination_class = MyPagination
#
#     def get(self, request, **kwargs):
#         """Adding logic for pagination"""
#         queryset = Habit.objects.filter(habit_is_public=True)
#         paginated_queryset = self.paginate_queryset(queryset)
#         serializer = HabitSerializer(paginated_queryset, many=True)
#         return self.get_paginated_response(serializer.data)
#
#
class BooksUserListAPIView(generics.ListAPIView):
    """View to create a list of books for particular user"""

    serializer_class = BookDetailSerializer
    queryset = BookDetail.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]  # an access only for user
    # pagination_class = MyPagination
#
    def get_queryset(self):
#
        return BookDetail.objects.filter(client=self.request.user)
#
#     def get(self, request, **kwargs):
#         """Adding logic for pagination"""
#         queryset = Habit.objects.filter(habit_user=self.request.user)
#         paginated_queryset = self.paginate_queryset(queryset)
#         serializer = HabitSerializer(paginated_queryset, many=True)
#         return self.get_paginated_response(serializer.data)
#
#
class BookRetrieveAPIView(generics.RetrieveAPIView):
    """View to get a particular habit for the user"""

    serializer_class = BookDetailSerializer
    queryset = BookDetail.objects.all()
    # permission_classes = [IsAuthenticated, IsOwner]  # an access only for user
#
#
# #
# #
class BookUpdateAPIView(generics.UpdateAPIView):
    """View to update a particular book"""

    serializer_class = BookDetailSerializer
    queryset = BookDetail.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarianAddBook]  # an access only for librarian
#
#
class BookDestroyAPIView(generics.DestroyAPIView):
    """View to delete a particular book"""

    queryset = BookDetail.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarianAddBook]  # an access only for librarian
#
#
# class PublicAPIView(APIView):
#     serializer_class = HabitSerializer
#     queryset = Habit.objects.all()
#
#     def post(self, view, pk):
#         """ View to make the habit publicly available or unavailable
#             only for the user of the habit."""
#         message = ""
#
#         if Habit.objects.filter(
#             pk=pk, habit_user=self.request.user
#         ).exists():  # In case if habit belongs to particular user
#
#             habit = get_object_or_404(
#                 Habit, id=pk
#             )  # get a particular habit via request
#
#             if habit.habit_is_public:
#                 habit.habit_is_public = False
#                 habit.save()
#                 message = "Habit is not public anymore"
#
#             elif not habit.habit_is_public:
#                 habit.habit_is_public = True
#                 habit.save()
#                 message = "Habit is publicly available now"
#
#             return Response({"message": {message}}, status=status.HTTP_201_CREATED)
#         return HttpResponseForbidden(
#             "You do not have permission to change a status of public availability"
#         )



class AuthorCreateAPIView(generics.CreateAPIView):
    """View to create a author"""

    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, IsLibrarianAddBook]

#
class AuthorsListAPIView(generics.ListAPIView):
    """View to create a list of authors"""

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorRetrieveAPIView(generics.RetrieveAPIView):
    """View to get a particular author"""

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorUpdateAPIView(generics.UpdateAPIView):
    """View to update a particular Author"""

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarianAddBook]  # an access only for librarian
#
#
class AuthorDestroyAPIView(generics.DestroyAPIView):
    """View to delete a particular Author"""

    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarianAddBook]  # an access only for librarian


class BookGeneralCreateAPIView(generics.CreateAPIView):
    """View to create a general book description"""

    serializer_class = BookGeneralSerializer
    permission_classes = [IsAuthenticated, IsLibrarianAddBook]

#
class BookGeneralsListAPIView(generics.ListAPIView):
    """View to create a list of general books descriptions"""

    serializer_class = BookGeneralSerializer
    queryset = BookGeneral.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarianAddBook]


class BookGeneralRetrieveAPIView(generics.RetrieveAPIView):
    """View to get a particular general book description"""

    serializer_class = BookGeneralSerializer
    queryset = BookGeneral.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarianAddBook]


class BookGeneralUpdateAPIView(generics.UpdateAPIView):
    """View to update a particular general book description"""

    serializer_class = BookGeneralSerializer
    queryset = BookGeneral.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarianAddBook]  # an access only for librarian
#
#
class BookGeneralDestroyAPIView(generics.DestroyAPIView):
    """View to delete a particular general book description"""

    queryset = BookGeneral.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarianAddBook]  # an access only for librarian



class LibraryCreateAPIView(generics.CreateAPIView):
    """View to create a library"""

    serializer_class = LibrarySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

#
class LibrariesListAPIView(generics.ListAPIView):
    """View to create a list of libraries"""

    serializer_class = LibrarySerializer
    queryset = Library.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class LibraryRetrieveAPIView(generics.RetrieveAPIView):
    """View to get a particular library"""

    serializer_class = LibrarySerializer
    queryset = Library.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class LibraryUpdateAPIView(generics.UpdateAPIView):
    """View to update a particular library"""

    serializer_class = LibrarySerializer
    queryset = Library.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]  # an access only for admin
#
#
class LibraryDestroyAPIView(generics.DestroyAPIView):
    """View to delete a particular library"""

    queryset = Library.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarianAddBook]  # an access only for admin



class GenreCreateAPIView(generics.CreateAPIView):
    """View to create a genre"""

    serializer_class = BookGenreSerializer
    permission_classes = [IsAuthenticated, IsLibrarianAddBook]

#
class GenresListAPIView(generics.ListAPIView):
    """View to create a list of genres"""

    serializer_class = BookGenreSerializer
    queryset = BookGenre.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarianAddBook]


class GenreRetrieveAPIView(generics.RetrieveAPIView):
    """View to get a particular genre"""

    serializer_class = BookGenreSerializer
    queryset = BookGenre.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarianAddBook]


class GenreUpdateAPIView(generics.UpdateAPIView):
    """View to update a particular genre"""

    serializer_class = BookGenreSerializer
    queryset = BookGenre.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarianAddBook]  # an access only for librarian
#
#
class GenreDestroyAPIView(generics.DestroyAPIView):
    """View to delete a particular genre"""

    queryset = BookGenre.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarianAddBook]  # an access only for librarian


class BookFinanceCreateAPIView(generics.CreateAPIView):
    """View to create a book finance"""

    serializer_class = BookFinanceSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

#
class BookFinancesListAPIView(generics.ListAPIView):
    """View to create a list of book finances"""

    serializer_class = BookFinanceSerializer
    queryset = BookFinance.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class BookFinanceRetrieveAPIView(generics.RetrieveAPIView):
    """View to get a particular book finance"""

    serializer_class = BookFinanceSerializer
    queryset = BookFinance.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]


class BookFinanceUpdateAPIView(generics.UpdateAPIView):
    """View to update a particular book finance"""

    serializer_class = BookFinanceSerializer
    queryset = BookFinance.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]  # an access only for admin
#
#
class BookFinanceDestroyAPIView(generics.DestroyAPIView):
    """View to delete a particular book finance"""

    queryset = BookFinance.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]  # an access only for admin