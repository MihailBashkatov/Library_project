from django.db import models

from users.models import User


# Create Model Library
class Library(models.Model):

    name = models.CharField(
        unique=True,
        max_length=300,
        verbose_name="Library name",
    )

    main_page = models.TextField(
        help_text="Main page text", verbose_name="Main page text"
    )
    rules_page = models.TextField(
        help_text="Rules page text", verbose_name="Rules page text"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Library"
        verbose_name_plural = "Libraries"


# Create Model Author
class Author(models.Model):
    name = models.CharField(
        max_length=300,
        verbose_name="Author name",
    )
    surname = models.CharField(
        max_length=300,
        verbose_name="Author surname",
    )
    birth_date = models.DateField(
        auto_now=False, null=False, blank=False, verbose_name="Author's birthday"
    )

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


# # Create Model BookGenre
# class BookGenre(models.Model):
#     ADVENTURE = "Adventure"
#     KIDS = "Kids"
#     CLASSIC = "Classic"
#     FOREIGN_LANGUAGE = "Foreign_language"
#     FANTASY = "Fantasy"
#     SCIENCE = "Science"
#     MIX = "Mix"
#
#     STATUS_CHOICES = [
#         (ADVENTURE, "Adventure"),
#         (KIDS, "Kids"),
#         (CLASSIC, "Classic"),
#         (FOREIGN_LANGUAGE, "Foreign_language"),
#         (FANTASY, "Fantasy"),
#         (SCIENCE, "Science"),
#         (MIX, "Mix"),
#     ]
#
#     genre = models.CharField(
#         max_length=16,
#         choices=STATUS_CHOICES,
#         verbose_name="Book genre",
#         null=False,
#         blank=False
#     )
#
#     def __str__(self):
#         return self.genre
#
#     class Meta:
#         verbose_name = "Genre"
#         verbose_name_plural = "Genres"


# Create Model BookGenre
class BookGenre(models.Model):

    genre = models.CharField(
        max_length=16,
        null=False,
        blank=False,
        verbose_name="Book genre",
    )

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


# Create Model BookFeature
class BookFeature(models.Model):
    RARE = "Rare"
    EXPENSIVE = "Expensive"
    NO_FEATURES = "No_features"

    STATUS_CHOICES = [
        (RARE, "Rare"),
        (EXPENSIVE, "Expensive"),
        (NO_FEATURES, "No_features"),
    ]

    feature = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES,
        default=NO_FEATURES,
        verbose_name="Book feature",
    )

    def __str__(self):
        return self.feature

    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"


# Create Model BookGeneral
class BookGeneral(models.Model):
    library = models.ForeignKey(
        Library,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="library",
    )

    title = models.CharField(
        max_length=300,
        verbose_name="Book Title",
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
        related_name="author",
    )

    description = models.TextField(
        help_text="Book description", verbose_name="Book description"
    )

    age_restriction = models.PositiveSmallIntegerField(
        null=False, blank=False, verbose_name="Age restriction"
    )

    rating = models.PositiveIntegerField(
        default=0, null=False, blank=False, verbose_name="Book rating"
    )

    is_available = models.BooleanField(default=True)

    # genre = models.ForeignKey(
    #     BookGenre,
    #     on_delete=models.DO_NOTHING,
    #     null=False,
    #     blank=False,
    #     related_name="book_genre",
    # )

    genre = models.ForeignKey(
        BookGenre,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="genre_book",
    )

    is_book_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


# Create Model BookDetail
class BookDetail(models.Model):

    book_general = models.ForeignKey(
        BookGeneral,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="book_detail",
    )

    client = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="client",
    )

    edition_year = models.DateField(
        auto_now=False, null=False, blank=False, verbose_name="Edition date"
    )

    page_amount = models.PositiveSmallIntegerField(
        verbose_name="Amount of pages", null=False, blank=False
    )

    taken_by_client = models.DateTimeField(
        auto_now=False,
        null=True,
        blank=True,
        default=None,
        verbose_name="Date, when Taken by client",
    )

    due_date = models.DateTimeField(
        auto_now=False,
        null=True,
        blank=True,
        verbose_name="Date, when shall be return by client",
    )

    is_overdue = models.BooleanField(default=False)

    picture = models.ImageField(
        upload_to="books/pictures/%Y/%m/%d/",
        default=None,
        null=True,
        blank=True,
        verbose_name="Saved boo picture",
    )

    feature = models.ForeignKey(
        BookFeature,
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
        related_name="book_feature",
    )

    def __str__(self):
        return self.book_general.title

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


# Create Model BookVolume
class BookVolume(models.Model):
    number = models.PositiveSmallIntegerField(
        null=False, blank=False, verbose_name="Volume number"
    )

    page_amount = models.PositiveSmallIntegerField(
        verbose_name="Amount of pages", null=False, blank=False
    )

    book = models.ForeignKey(
        BookDetail,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="book_volume",
    )

    def __str__(self):
        return f'{self.number}'

    class Meta:
        verbose_name = "Volume"
        verbose_name_plural = "Volumes"


# Create Model BookFinance
class BookFinance(models.Model):

    book = models.OneToOneField(
        BookDetail,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="book_finance",
    )

    price = models.FloatField(null=False, blank=False, verbose_name="Book price")
    overdue_day = models.PositiveSmallIntegerField(
        default=0, null=False, blank=False, verbose_name="Overdue day for the book"
    )
    overdue_date = models.DateTimeField(
        auto_now=False, null=True, blank=True, verbose_name="Start date of overdue"
    )
    penalty_sum = models.FloatField(
        default=0, null=False, blank=False, verbose_name="Penalty for overdue"
    )
    end_overdue = models.DateTimeField(
        auto_now=False, null=True, blank=True, verbose_name="End date of overdue"
    )
    is_payment_done = models.BooleanField(default=None, null=True, blank=True)

    def __str__(self):
        return self.price

    class Meta:
        verbose_name = "Finance"
        verbose_name_plural = "Finances"


# Create Model BookContent
class BookContent(models.Model):
    book = models.ForeignKey(BookDetail,
                             null=True,
                             blank=True,
                             on_delete=models.CASCADE,
                             related_name="book_content")

    volume = models.ForeignKey(BookVolume,
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE,
                               related_name="volume_content")

    number = models.CharField(
        max_length=100,
        verbose_name=" Number text",
    )
    content = models.CharField(
        max_length=100,
        verbose_name="Content text",
    )

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Content"
        verbose_name_plural = "Contents"

# class HistoryBookDetailPerClient(models.Model):
#
#     book = models.ForeignKey(
#         BookDetail,
#         on_delete=models.DO_NOTHING,
#         null=True,
#         blank=True,
#         related_name="book_detail",
#     )
#
#     client = models.ForeignKey(
#         User,
#         on_delete=models.DO_NOTHING,
#         null=True,
#         blank=True,
#         related_name="client",
#     )
#
#     taken_by_client = models.DateTimeField(
#         auto_now=False, null=True, blank=True, default=None, verbose_name="Date, when Taken by client"
#     )
#
#     return_date = models.DateTimeField(
#         auto_now=False,
#         null=True,
#         blank=True,
#         verbose_name="Date, when shall be return by client",
#     )
#
#     is_overdue = models.BooleanField(default=False)
#
#     is_payment_done = models.BooleanField(default=None)
#
#     def __str__(self):
#         return self.book
#
#     class Meta:
#         verbose_name = "Book"
#         verbose_name_plural = "Books"
