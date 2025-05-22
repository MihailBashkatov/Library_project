from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the model User."""

    class Meta:
        model = User
        fields = ["id", "email", "user_card", "telegram_chat_id"]
