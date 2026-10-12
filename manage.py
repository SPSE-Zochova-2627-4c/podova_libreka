"""Minimal Django runner for the Libreka school project.

This file keeps the project runnable even though it does not yet have the
standard Django package layout with separate settings, urls and views modules.
"""

from pathlib import Path
import os
import sys


BASE_DIR = Path(__file__).resolve().parent


def setup_settings() -> None:
    """Configure Django settings for this small single-file project."""
    from django.conf import settings

    if settings.configured:
        return

    settings.configure(
        DEBUG=True,
        SECRET_KEY="libreka-dev-secret-key",
        ROOT_URLCONF=__name__,
        ALLOWED_HOSTS=["127.0.0.1", "localhost"],
        INSTALLED_APPS=[
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.staticfiles",
            "libreka",
        ],
        MIDDLEWARE=[
            "django.middleware.security.SecurityMiddleware",
            "django.contrib.sessions.middleware.SessionMiddleware",
            "django.middleware.common.CommonMiddleware",
            "django.middleware.csrf.CsrfViewMiddleware",
            "django.contrib.auth.middleware.AuthenticationMiddleware",
            "django.contrib.messages.middleware.MessageMiddleware",
            "django.middleware.clickjacking.XFrameOptionsMiddleware",
        ],
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": BASE_DIR / "db.sqlite3",
            }
        },
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": [BASE_DIR / "templates"],
                "APP_DIRS": True,
                "OPTIONS": {
                    "context_processors": [
                        "django.template.context_processors.request",
                        "django.contrib.auth.context_processors.auth",
                        "django.contrib.messages.context_processors.messages",
                    ],
                },
            }
        ],
        STATIC_URL="static/",
        STATICFILES_DIRS=[BASE_DIR / "static"] if (BASE_DIR / "static").exists() else [],
        DEFAULT_AUTO_FIELD="django.db.models.BigAutoField",
    )


setup_settings()

import django

django.setup()

from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import path


def home(request):
    return render(request, "_base.html")


def login_view(request):
    if request.method == "POST":
        return redirect("profile")

    return render(request, "login.html")


def profile_view(request):
    return render(request, "profile.html")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("login/", login_view, name="login"),
    path("profile/", profile_view, name="profile"),
]


def main() -> None:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", __name__)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
