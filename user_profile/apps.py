"""App configuration."""

from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    """User profile config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "user_profile"
