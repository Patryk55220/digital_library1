# library/urls.py
from django.urls import path
from . import views                  # importujemy moduł z widokami
from .views import ProfileView       # lub views.ProfileView

app_name = "library"

urlpatterns = [
    # lista książek (strona główna aplikacji)
    path("",                      views.BookListView.as_view(),      name="book-list"),

    # CRUD dla książki
    path("book/<int:pk>/",        views.BookDetailView.as_view(),    name="book-detail"),
    path("book/add/",             views.BookCreateView.as_view(),    name="book-add"),
    path("book/<int:pk>/edit/",   views.BookUpdateView.as_view(),    name="book-edit"),
    path("book/<int:pk>/delete/", views.BookDeleteView.as_view(),    name="book-delete"),

    # wypożyczanie / zwroty
    path("book/<int:pk>/loan/",   views.LoanCreateView.as_view(),    name="loan-create"),
    path("book/<int:pk>/return/", views.LoanReturnView.as_view(),    name="loan-return"),

    # profil zalogowanego użytkownika
    path("accounts/profile/",     ProfileView.as_view(),             name="profile"),
]
