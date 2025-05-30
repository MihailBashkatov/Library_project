from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from books.models import (Archive, Author, BookContent, BookDetail,
                          BookFeature, BookFinance, BookGeneral, BookGenre,
                          BookVolume, Library)
from books.permissions import IsLibrarian, IsOwner
from books.serializers import (ArchiveOrderSerializer, AuthorSerializer,
                               BookContentSerializer,
                               BookDetailClientSerializer,
                               BookDetailSerializer, BookFeatureSerializer,
                               BookFinanceSerializer, BookGeneralSerializer,
                               BookGenreSerializer, BookVolumeSerializer,
                               LibrarySerializer, BookPublicSerializer)


class BookCreateAPIView(generics.CreateAPIView):
    """View to create a book"""

    serializer_class = BookDetailSerializer
    permission_classes = [IsAuthenticated, IsLibrarian]


class BooksListAPIView(generics.ListAPIView):
    """View to create a list of books for librarian and admin"""

    serializer_class = BookDetailSerializer
    queryset = BookDetail.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsLibrarian | IsAdminUser,
    ]  # an access only for librarian and admin
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = (
        "book_general",
        "client",
        "edition_year",
        "page_amount",
        "taken_by_client",
        "due_date",
        "is_overdue",
        "book_content",
        "feature",
        "book_finance",
        "book_volume",
    )

    ordering_fields = (
        "book_general",
        "client",
        "edition_year",
        "page_amount",
        "taken_by_client",
        "due_date",
        "is_overdue",
        "book_content",
        "feature",
        "book_finance",
        "book_volume",
    )

    search_fields = (
        "book_general__title",
        "book_general__description",
        "client__email",
        "edition_year",
        "page_amount",
        "taken_by_client",
        "due_date",
        "is_overdue",
        "book_content__content",
        "feature__feature",
        "book_finance__price",
        "book_volume__number",
    )


class BooksUserListAPIView(generics.ListAPIView):
    """View to create a list of books for particular user"""

    serializer_class = BookDetailSerializer
    queryset = BookDetail.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]  # an access only for user
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = (
        "book_general",
        "edition_year",
        "page_amount",
        "taken_by_client",
        "due_date",
        "is_overdue",
        "book_content",
        "feature",
        "book_finance",
        "book_volume",
    )

    ordering_fields = (
        "book_general",
        "edition_year",
        "page_amount",
        "taken_by_client",
        "due_date",
        "is_overdue",
        "book_content",
        "feature",
        "book_finance",
        "book_volume",
    )

    search_fields = (
        "book_general",
        "edition_year",
        "page_amount",
        "taken_by_client",
        "due_date",
        "is_overdue",
        "book_content",
        "feature",
        "book_finance",
        "book_volume",
    )

    def get_queryset(self):

        return BookDetail.objects.filter(client=self.request.user)


class BookRetrieveAPIView(generics.RetrieveAPIView):
    """View to get a particular book for the librarian and adminr"""

    serializer_class = BookDetailSerializer
    queryset = BookDetail.objects.all()
    permission_classes = [
        IsAuthenticated,
        IsLibrarian | IsAdminUser,
    ]  # an access only for librarian and admin


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
    permission_classes = [AllowAny,]  # access for all

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ("name", "surname", "birth_date")
    ordering_fields = ("name", "surname", "birth_date")
    search_fields = ("name", "surname", "birth_date")


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
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = (
        "library",
        "title",
        "author",
        "age_restriction",
        "rating",
        "is_available",
        "genre",
        "is_book_popular",
    )

    ordering_fields = (
        "library",
        "title",
        "author",
        "age_restriction",
        "rating",
        "is_available",
        "genre",
        "is_book_popular",
    )

    search_fields = (
        "title",
        "author__name",
        "author__surname",
        "description",
        "age_restriction",
        "rating",
        "genre__genre",
        "is_book_popular",
    )


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

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ("genre",)
    ordering_fields = ("genre",)
    search_fields = ("genre",)


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

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = (
        "book",
        "price",
        "overdue_date",
        "penalty_sum",
    )

    ordering_fields = (
        "book",
        "price",
        "overdue_date",
        "penalty_sum",
    )

    search_fields = (
        "price",
        "overdue_date",
        "penalty_sum",
    )


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

    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ("content",)


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
    permission_classes = [
        IsAuthenticated,
        IsLibrarian | IsAdminUser,
    ]  # an access only for librarian and admin

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]

    filterset_fields = (
        "order",
        "title",
        "user_card",
        "taken_by_client",
        "return_date",
        "order_continued_times",
        "is_overdue",
        "payment_date",
        "payed_sum",
    )
    ordering_fields = (
        "order",
        "title",
        "user_card",
        "taken_by_client",
        "return_date",
        "order_continued_times",
        "is_overdue",
        "payment_date",
        "payed_sum",
    )

    search_fields = (
        "title",
        "user_card",
        "taken_by_client",
        "return_date",
        "payment_date",
        "payed_sum",
    )


class ClientArchiveOrderListAPIView(generics.ListAPIView):
    """View to create a list of ordered books for particular client"""

    serializer_class = ArchiveOrderSerializer
    queryset = Archive.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]  # an access only for user
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]

    filterset_fields = (
        "order",
        "title",
        "user_card",
        "taken_by_client",
        "return_date",
        "order_continued_times",
    )
    ordering_fields = (
        "order",
        "title",
        "user_card",
        "taken_by_client",
        "return_date",
        "order_continued_times",
    )

    search_fields = (
        "title",
        "user_card",
        "taken_by_client",
        "return_date",
    )

    def get_queryset(self):

        return Archive.objects.filter(user_card=self.request.user.user_card)


class BookPublicListAPIView(generics.ListAPIView):
    """View to create a list of public books"""

    serializer_class = BookPublicSerializer
    queryset = BookDetail.objects.all()
    permission_classes = [
        AllowAny,
    ]  # an access for all
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = (
        "book_general",
        "edition_year",
        "page_amount",
        "book_content",
        "feature",
        "book_volume",
    )

    ordering_fields = (
        "book_general",
        "edition_year",
        "page_amount",
        "book_content",
        "feature",
        "book_volume",
    )

    search_fields = (
        "book_general__title",
        "book_general__description",
        "edition_year",
        "page_amount",
        "book_content__content",
        "feature__feature",
        "book_volume__number",
    )


class BookPublicRetrieveAPIView(generics.RetrieveAPIView):
    """View to get a particular book for all"""

    serializer_class = BookPublicSerializer
    queryset = BookDetail.objects.all()
    permission_classes = [AllowAny]  # an access for all


class BooksUserRetrieveAPIView(generics.RetrieveAPIView):
    """View to get a particular book for  particular user"""

    serializer_class = BookDetailSerializer
    queryset = BookDetail.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]  # an access only for user

    def get_queryset(self):

        return BookDetail.objects.filter(client=self.request.user)
