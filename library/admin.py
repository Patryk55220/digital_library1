from django.contrib import admin
from .models import Author, Book, Loan

# Poprawiony admin dla Author
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)  # tylko jedno pole: name

# Poprawiony admin dla Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year')
    search_fields = ('title',)

# Poprawiony admin dla Loan
@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'date')  # użyj 'date', nie 'borrowed_at'
    list_filter = ('date',)                  # użyj 'date', nie 'borrowed_at'
