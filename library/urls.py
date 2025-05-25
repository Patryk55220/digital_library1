from django.urls import path
from .views import (
    BookListView, BookDetailView,
    BookCreateView, BookUpdateView, BookDeleteView,
    LoanCreateView, LoanReturnView,
    ProfileView,
)

app_name = 'library'

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/add/', BookCreateView.as_view(), name='book-add'),
    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='book-edit'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('book/<int:pk>/loan/', LoanCreateView.as_view(), name='loan-create'),
    path('book/<int:pk>/return/', LoanReturnView.as_view(), name='loan-return'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
]
