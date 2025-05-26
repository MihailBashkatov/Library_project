from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from books.models import (
    Author,
    BookDetail,
    BookFinance,
    BookGeneral,
    BookGenre,
    Library,
    BookVolume,
    BookContent,
    BookFeature,
    Archive,
)
from books.permissions import IsLibrarian, IsOwner
from books.serializers import (
    AuthorSerializer,
    BookDetailSerializer,
    BookFinanceSerializer,
    BookGeneralSerializer,
    BookGenreSerializer,
    LibrarySerializer,
    BookVolumeSerializer,
    BookContentSerializer,
    BookFeatureSerializer,
    BookDetailClientSerializer,
    ArchiveOrderSerializer,
)


#
class BookCreateAPIView(generics.CreateAPIView):
    """View to create a book"""

    serializer_class = BookDetailSerializer
    permission_classes = [IsAuthenticated, IsLibrarian]


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
    permission_classes = [
        IsAuthenticated,
        IsLibrarian,
    ]  # an access only for librarian


#
#
class BookDestroyAPIView(generics.DestroyAPIView):
    """View to delete a particular book"""

    queryset = BookDetail.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsLibrarian,
    ]  # an access only for librarian


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
    permission_classes = [IsAuthenticated, IsLibrarian]


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
    permission_classes = [
        IsAuthenticated,
        IsLibrarian,
    ]  # an access only for librarian


#
#
class AuthorDestroyAPIView(generics.DestroyAPIView):
    """View to delete a particular Author"""

    queryset = Author.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsLibrarian,
    ]  # an access only for librarian


class BookGeneralCreateAPIView(generics.CreateAPIView):
    """View to create a general book description"""

    serializer_class = BookGeneralSerializer
    permission_classes = [IsAuthenticated, IsLibrarian]


#
class BookGeneralsListAPIView(generics.ListAPIView):
    """View to create a list of general books descriptions"""

    serializer_class = BookGeneralSerializer
    queryset = BookGeneral.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarian]


class BookGeneralRetrieveAPIView(generics.RetrieveAPIView):
    """View to get a particular general book description"""

    serializer_class = BookGeneralSerializer
    queryset = BookGeneral.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarian]


class BookGeneralUpdateAPIView(generics.UpdateAPIView):
    """View to update a particular general book description"""

    serializer_class = BookGeneralSerializer
    queryset = BookGeneral.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsLibrarian,
    ]  # an access only for librarian


#
#
class BookGeneralDestroyAPIView(generics.DestroyAPIView):
    """View to delete a particular general book description"""

    queryset = BookGeneral.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsLibrarian,
    ]  # an access only for librarian


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


class LibraryDestroyAPIView(generics.DestroyAPIView):
    """View to delete a particular library"""

    queryset = Library.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsLibrarian,
    ]  # an access only for admin


class GenreCreateAPIView(generics.CreateAPIView):
    """View to create a genre"""

    serializer_class = BookGenreSerializer
    permission_classes = [IsAuthenticated, IsLibrarian]


#
class GenresListAPIView(generics.ListAPIView):
    """View to create a list of genres"""

    serializer_class = BookGenreSerializer
    queryset = BookGenre.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarian]


class GenreRetrieveAPIView(generics.RetrieveAPIView):
    """View to get a particular genre"""

    serializer_class = BookGenreSerializer
    queryset = BookGenre.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarian]


class GenreUpdateAPIView(generics.UpdateAPIView):
    """View to update a particular genre"""

    serializer_class = BookGenreSerializer
    queryset = BookGenre.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsLibrarian,
    ]  # an access only for librarian


#
#
class GenreDestroyAPIView(generics.DestroyAPIView):
    """View to delete a particular genre"""

    queryset = BookGenre.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsLibrarian,
    ]  # an access only for librarian


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


class BookVolumeCreateAPIView(generics.CreateAPIView):
    """View to create a book volume"""

    serializer_class = BookVolumeSerializer
    permission_classes = [IsAuthenticated, IsLibrarian]


#
class BookVolumesListAPIView(generics.ListAPIView):
    """View to create a list of book volumes"""

    serializer_class = BookVolumeSerializer
    queryset = BookVolume.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarian]


class BookVolumeRetrieveAPIView(generics.RetrieveAPIView):
    """View to get a particular book volume"""

    serializer_class = BookVolumeSerializer
    queryset = BookVolume.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarian]


class BookVolumeUpdateAPIView(generics.UpdateAPIView):
    """View to update a particular book volume"""

    serializer_class = BookVolumeSerializer
    queryset = BookVolume.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarian]  # an access only for librarian


class BookVolumeDestroyAPIView(generics.DestroyAPIView):
    """View to delete a particular book volume"""

    queryset = BookVolume.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarian]  # an access only for librarian


class BookContentCreateAPIView(generics.CreateAPIView):
    """View to create a book content"""

    serializer_class = BookContentSerializer
    permission_classes = [IsAuthenticated, IsLibrarian]


class BookContentsListAPIView(generics.ListAPIView):
    """View to create a list of book contents"""

    serializer_class = BookContentSerializer
    queryset = BookContent.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarian]


class BookContentRetrieveAPIView(generics.RetrieveAPIView):
    """View to get a particular book content"""

    serializer_class = BookContentSerializer
    queryset = BookContent.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarian]


class BookContentUpdateAPIView(generics.UpdateAPIView):
    """View to update a particular book content"""

    serializer_class = BookContentSerializer
    queryset = BookContent.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarian]  # an access only for librarian


class BookContentDestroyAPIView(generics.DestroyAPIView):
    """View to delete a particular book content"""

    queryset = BookContent.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarian]  # an access only for librarian


class BookFeatureCreateAPIView(generics.CreateAPIView):
    """View to create a book feature"""

    serializer_class = BookFeatureSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]  # an access only for admin


class BookFeaturesListAPIView(generics.ListAPIView):
    """View to create a list of book features"""

    serializer_class = BookFeatureSerializer
    queryset = BookFeature.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]  # an access only for admin


class BookFeatureRetrieveAPIView(generics.RetrieveAPIView):
    """View to get a particular book feature"""

    serializer_class = BookFeatureSerializer
    queryset = BookFeature.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]  # an access only for admin


class BookFeatureUpdateAPIView(generics.UpdateAPIView):
    """View to update a particular book feature"""

    serializer_class = BookFeatureSerializer
    queryset = BookFeature.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]  # an access only for admin


class BookFeatureDestroyAPIView(generics.DestroyAPIView):
    """View to delete a particular book feature"""

    queryset = BookFeature.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]  # an access only for admin


class BookUpdateClientAPIView(generics.UpdateAPIView):
    """View to update a particular book when takes or return by client"""

    serializer_class = BookDetailClientSerializer
    queryset = BookDetail.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsLibrarian,
    ]  # an access only for librarian


class ArchiveOrderListAPIView(generics.ListAPIView):
    """View to get list of archive orders"""

    serializer_class = ArchiveOrderSerializer
    queryset = Archive.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsLibrarian | IsAdminUser,
    ]  # an access only for librarian and admin


class ClientArchiveOrderListAPIView(generics.ListAPIView):
    """View to create a list of ordered books for particular client"""

    serializer_class = ArchiveOrderSerializer
    queryset = Archive.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]  # an access only for user
    # pagination_class = MyPagination

    def get_queryset(self):

        return Archive.objects.filter(user_card=self.request.user.user_card)

    # def get(self, request, **kwargs):
    #     """Adding logic for pagination"""
    #     queryset = Habit.objects.filter(habit_user=self.request.user)
    #     paginated_queryset = self.paginate_queryset(queryset)
    #     serializer = HabitSerializer(paginated_queryset, many=True)
    #     return self.get_paginated_response(serializer.data)
