from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the model User."""

    class Meta:
        model = User
        fields = ["id", "email", "user_card", "telegram_chat_id"]

    def create(self, validated_data):
        """Create users_card for the user"""
        user_card = []
        last_user_card = str(User.objects.all().last().id + 1)
        if len(last_user_card) == 1:
            user_card = "".join(["0", "0", "0", last_user_card[0]])
        elif len(last_user_card) == 2:
            user_card = "".join(["0", "0", last_user_card[0], last_user_card[1]])
        elif len(last_user_card) == 3:
            user_card = "".join(
                ["0", last_user_card[0], last_user_card[1], last_user_card[2]]
            )
        elif len(last_user_card) == 4:
            user_card = "".join(
                [
                    last_user_card[0],
                    last_user_card[1],
                    last_user_card[2],
                    last_user_card[3],
                ]
            )

        validated_data["user_card"] = user_card

        return User.objects.create(**validated_data)
