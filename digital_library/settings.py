from pathlib import Path
import os, dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("SECRET_KEY", "changeme")
DEBUG = os.getenv("DEBUG", "True") == "True"
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "library",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "digital_library.urls"
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [BASE_DIR / "library" / "templates"],
    "APP_DIRS": True,
    "OPTIONS": {"context_processors": [
        "django.template.context_processors.debug",
        "django.template.context_processors.request",
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
    ]},
}]

WSGI_APPLICATION = "digital_library.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'digital_library'),
        'USER': os.environ.get('POSTGRES_USER', 'dl_user'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'secret'),
        'HOST': 'db',  # nazwa serwisu z docker-compose
        'PORT': 5432,
    }
}


AUTH_PASSWORD_VALIDATORS = [{
    "NAME":"django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME":"django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME":"django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME":"django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "pl-pl"
TIME_ZONE = "Europe/Warsaw"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

from django.urls import reverse_lazy   # na samej górze pliku, razem z innymi importami


LOGOUT_REDIRECT_URL = '/accounts/login/'
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
DEBUG = True

