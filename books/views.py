from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from books.models import (Archive, Author, BookContent, BookDetail,
                          BookFeature, BookFinance, BookGeneral, BookGenre,
                          BookVolume, Library)
from books.paginators import MyPagination
from books.permissions import IsLibrarian, IsOwner
from books.serializers import (ArchiveOrderSerializer, AuthorSerializer,
                               BookContentSerializer,
                               BookDetailClientSerializer,
                               BookDetailSerializer, BookFeatureSerializer,
                               BookFinanceSerializer, BookGeneralSerializer,
                               BookGenreSerializer, BookVolumeSerializer,
                               LibrarySerializer)


class BookCreateAPIView(generics.CreateAPIView):
    """View to create a book"""

    serializer_class = BookDetailSerializer
    permission_classes = [IsAuthenticated, IsLibrarian]


class BooksListAPIView(generics.ListAPIView):
    """View to create a list of public books"""

    serializer_class = BookDetailSerializer
    queryset = BookDetail.objects.all()
    permission_classes = [
        AllowAny,
    ]  # access for all users
    pagination_class = MyPagination

    def get(self, request, **kwargs):
        """Adding logic for pagination"""
        queryset = BookDetail.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = BookDetailSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class BooksUserListAPIView(generics.ListAPIView):
    """View to create a list of books for particular user"""

    serializer_class = BookDetailSerializer
    queryset = BookDetail.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]  # an access only for user
    pagination_class = MyPagination

    def get_queryset(self):
        return BookDetail.objects.filter(client=self.request.user)

    def get(self, request, **kwargs):
        """Adding logic for pagination"""
        queryset = BookDetail.objects.filter(client=self.request.user)
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = BookDetailSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class BookRetrieveAPIView(generics.RetrieveAPIView):
    """View to get a particular book for the user"""

    serializer_class = BookDetailSerializer
    queryset = BookDetail.objects.all()
    permission_classes = [
        AllowAny,
    ]  # access for all


class BookUpdateAPIView(generics.UpdateAPIView):
    """View to update a particular book"""

    serializer_class = BookDetailSerializer
    queryset = BookDetail.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsLibrarian,
    ]  # an access only for librarian


class BookDestroyAPIView(generics.DestroyAPIView):
    """View to delete a particular book"""

    queryset = BookDetail.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsLibrarian,
    ]  # an access only for librarian


class AuthorCreateAPIView(generics.CreateAPIView):
    """View to create an author"""

    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated, IsLibrarian]  # an access only for librarian


class AuthorsListAPIView(generics.ListAPIView):
    """View to create a list of authors"""

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [
        AllowAny,
    ]  #  access for all
    pagination_class = MyPagination

    def get(self, request, **kwargs):
        """Adding logic for pagination"""
        queryset = Author.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = AuthorSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class AuthorRetrieveAPIView(generics.RetrieveAPIView):
    """View to get a particular author"""

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [
        AllowAny,
    ]  # access for all


class AuthorUpdateAPIView(generics.UpdateAPIView):
    """View to update a particular Author"""

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsLibrarian,
    ]  # an access only for librarian


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
    permission_classes = [IsAuthenticated, IsLibrarian]  # an access only for librarian


class BookGeneralsListAPIView(generics.ListAPIView):
    """View to create a list of general books descriptions"""

    serializer_class = BookGeneralSerializer
    queryset = BookGeneral.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsLibrarian,
    ]  # an access only for librarian
    pagination_class = MyPagination

    def get(self, request, **kwargs):
        """Adding logic for pagination"""
        queryset = BookGeneral.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = BookGeneralSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class BookGeneralRetrieveAPIView(generics.RetrieveAPIView):
    """View to get a particular general book description"""

    serializer_class = BookGeneralSerializer
    queryset = BookGeneral.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarian]  # an access only for librarian


class BookGeneralUpdateAPIView(generics.UpdateAPIView):
    """View to update a particular general book description"""

    serializer_class = BookGeneralSerializer
    queryset = BookGeneral.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsLibrarian,
    ]  # an access only for librarian


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
    permission_classes = [IsAuthenticated, IsAdminUser]  # an access only for admin


class LibrariesListAPIView(generics.ListAPIView):
    """View to create a list of libraries"""

    serializer_class = LibrarySerializer
    queryset = Library.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]  # an access only for admin


class LibraryRetrieveAPIView(generics.RetrieveAPIView):
    """View to get a particular library"""

    serializer_class = LibrarySerializer
    queryset = Library.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]  # an access only for admin


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
    permission_classes = [IsAuthenticated, IsLibrarian]  # an access only for librarian


class GenresListAPIView(generics.ListAPIView):
    """View to create a list of genres"""

    serializer_class = BookGenreSerializer
    queryset = BookGenre.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarian]  # an access only for librarian
    pagination_class = MyPagination

    def get(self, request, **kwargs):
        """Adding logic for pagination"""
        queryset = BookGenre.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = BookGenreSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class GenreRetrieveAPIView(generics.RetrieveAPIView):
    """View to get a particular genre"""

    serializer_class = BookGenreSerializer
    queryset = BookGenre.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarian]  # an access only for librarian


class GenreUpdateAPIView(generics.UpdateAPIView):
    """View to update a particular genre"""

    serializer_class = BookGenreSerializer
    queryset = BookGenre.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsLibrarian,
    ]  # an access only for librarian


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
    permission_classes = [IsAuthenticated, IsAdminUser]  # an access only for admin


class BookFinancesListAPIView(generics.ListAPIView):
    """View to create a list of book finances"""

    serializer_class = BookFinanceSerializer
    queryset = BookFinance.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]  # an access only for admin
    pagination_class = MyPagination

    def get(self, request, **kwargs):
        """Adding logic for pagination"""
        queryset = BookFinance.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = BookFinanceSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class BookFinanceRetrieveAPIView(generics.RetrieveAPIView):
    """View to get a particular book finance"""

    serializer_class = BookFinanceSerializer
    queryset = BookFinance.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]  # an access only for admin


class BookFinanceUpdateAPIView(generics.UpdateAPIView):
    """View to update a particular book finance"""

    serializer_class = BookFinanceSerializer
    queryset = BookFinance.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]  # an access only for admin


class BookFinanceDestroyAPIView(generics.DestroyAPIView):
    """View to delete a particular book finance"""

    queryset = BookFinance.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]  # an access only for admin


class BookVolumeCreateAPIView(generics.CreateAPIView):
    """View to create a book volume"""

    serializer_class = BookVolumeSerializer
    permission_classes = [IsAuthenticated, IsLibrarian]  # an access only for librarian


class BookVolumesListAPIView(generics.ListAPIView):
    """View to create a list of book volumes"""

    serializer_class = BookVolumeSerializer
    queryset = BookVolume.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarian]  # an access only for librarian
    pagination_class = MyPagination

    def get(self, request, **kwargs):
        """Adding logic for pagination"""
        queryset = BookVolume.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = BookVolumeSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class BookVolumeRetrieveAPIView(generics.RetrieveAPIView):
    """View to get a particular book volume"""

    serializer_class = BookVolumeSerializer
    queryset = BookVolume.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarian]  # an access only for librarian


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
    permission_classes = [IsAuthenticated, IsLibrarian]  # an access only for librarian


class BookContentsListAPIView(generics.ListAPIView):
    """View to create a list of book contents"""

    serializer_class = BookContentSerializer
    queryset = BookContent.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarian]  # an access only for librarian
    pagination_class = MyPagination

    def get(self, request, **kwargs):
        """Adding logic for pagination"""
        queryset = BookContent.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = BookContentSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class BookContentRetrieveAPIView(generics.RetrieveAPIView):
    """View to get a particular book content"""

    serializer_class = BookContentSerializer
    queryset = BookContent.objects.all()
    permission_classes = [IsAuthenticated, IsLibrarian]  # an access only for librarian


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
    pagination_class = MyPagination
    permission_classes = [
        IsAuthenticated,
        IsLibrarian | IsAdminUser,
    ]  # an access only for librarian and admin

    def get(self, request, **kwargs):
        """Adding logic for pagination"""
        queryset = Archive.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = ArchiveOrderSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class ClientArchiveOrderListAPIView(generics.ListAPIView):
    """View to create a list of ordered books for particular client"""

    serializer_class = ArchiveOrderSerializer
    queryset = Archive.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]  # an access only for user
    pagination_class = MyPagination

    def get_queryset(self):

        return Archive.objects.filter(user_card=self.request.user.user_card)

    def get(self, request, **kwargs):
        """Adding logic for pagination"""
        queryset = Archive.objects.filter(user_card=self.request.user)
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = ArchiveOrderSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)
