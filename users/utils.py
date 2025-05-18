from django.contrib.auth import get_user_model


def create_user():
    """ Creating users in database"""
    User = get_user_model()
    for user in range(1, 7):
        user = User.objects.create(
            email=f"user{user}@user.com",
        )

        user.set_password("1234")
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        user.save()
