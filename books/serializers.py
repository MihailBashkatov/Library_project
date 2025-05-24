# from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from books.models import (Author, BookContent, BookDetail, BookFeature,
                          BookFinance, BookGeneral, BookGenre, BookVolume,
                          Library, Archive)
from books.validators import IsBookTaken
from users.serializers import UserSerializer

# class HabitSerializer(serializers.ModelSerializer):
#     habit_date = serializers.DateTimeField(required=True,
#                                            input_formats=["%Y-%m-%d %H:%M"])
#     """Serializer for the model Habit."""
#     class Meta:
#         model = Habit
#         fields = "__all__"
#         validators = [
#             TimeDurationValidator(field=["habit_time_duration"]),
#             RewardOrHabitRelatedValidator(field=["related_habit", "habit_reward"]),
#             NiceHabitRelatedValidator(field=["related_habit"]),
#             NiceNotRewardNotRelatedHabitValidator(field=["is_nice_habit"]),
#             HabitPeriodValidator(field=["habit_period"]),
#
#         ]

class ArchiveOrderSerializer(serializers.ModelSerializer):
    """Serializer for the model Archive."""

    class Meta:
        model = Archive
        fields = "__all__"


class LibrarySerializer(serializers.ModelSerializer):
    """Serializer for the model Library."""

    class Meta:
        model = Library
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for the model Author."""

    class Meta:
        model = Author
        fields = "__all__"


class BookGenreSerializer(serializers.ModelSerializer):
    """Serializer for the model BookGenre."""

    class Meta:
        model = BookGenre
        fields = "__all__"


class BookFeatureSerializer(serializers.ModelSerializer):
    """Serializer for the model BookFeature."""

    class Meta:
        model = BookFeature
        fields = "__all__"


class BookContentSerializer(serializers.ModelSerializer):
    """Serializer for the model BookContent."""

    class Meta:
        model = BookContent
        fields = "__all__"


class BookFinanceSerializer(serializers.ModelSerializer):
    """Serializer for the model BookFinance."""

    class Meta:
        model = BookFinance
        fields = "__all__"


class BookVolumeSerializer(serializers.ModelSerializer):
    """Serializer for the model BookVolume."""

    volume_content = BookContentSerializer(read_only=True, many=True)

    class Meta:
        model = BookVolume
        fields = ["id", "number", "page_amount", "book", "volume_content"]


class BookGeneralSerializer(serializers.ModelSerializer):
    """Serializer for the model BookGeneral."""

    # genre = BookGenreSerializer(read_only=True, many=True)

    class Meta:
        model = BookGeneral
        fields = [
            "id",
            "library",
            "title",
            "author",
            "description",
            "age_restriction",
            "rating",
            "is_available",
            # "genre",
            "is_book_popular",
        ]


class BookDetailSerializer(serializers.ModelSerializer):
    """Serializer for the model BookDetail."""

    book_finance = BookFinanceSerializer(read_only=True)
    book_volume = BookVolumeSerializer(many=True, read_only=True)
    book_content = BookContentSerializer(read_only=True, many=True)
    book_general = BookGeneralSerializer(read_only=True)
    client = UserSerializer(read_only=True)
    taken_by_client = serializers.DateTimeField(required=True,
                                           input_formats=["%Y-%m-%d %H:%M"])

    def to_internal_value(self, data):
        book_general_pk = data.get("book_general")

        internal_data = super().to_internal_value(data)
        try:
            book_general = BookGeneral.objects.get(pk=book_general_pk)
        except BookGeneral.DoesNotExist:
            raise ValidationError(
                {"book_general": ["Invalid book_general primary key"]},
                code="invalid",
            )
        internal_data["book_general"] = book_general
        return internal_data

    class Meta:
        model = BookDetail
        fields = [
            "id",
            "book_general",
            "client",
            "edition_year",
            "page_amount",
            "taken_by_client",
            "due_date",
            "is_overdue",
            "picture",
            "book_content",
            "feature",
            "book_finance",
            "book_volume",
        ]

class BookDetailClientSerializer(serializers.ModelSerializer):
    """Serializer for the model BookDetail. If user takes or returns a book"""

    archive_order = ArchiveOrderSerializer(many=True, read_only=True)
    class Meta:
        model = BookDetail

        fields = [
            "client",
            "archive_order"
        ]

        validators = [
                    IsBookTaken(field=["client"]),
                ]
