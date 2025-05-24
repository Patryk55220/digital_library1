# digital_library/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Twoje URL-e aplikacji „library”
    path('', include('library.urls', namespace='library')),

    # wbudowane widoki logowania/wylogowania itp.
    path('accounts/', include('django.contrib.auth.urls')),
]
