from django.contrib import admin
from .models import Author, Book, Loan


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display  = ("last_name", "first_name")
    search_fields = ("last_name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display  = ("title", "author", "year")
    list_filter   = ("author", "year")
    search_fields = ("title", "author__last_name")


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ("book", "user", "borrowed_at", "due_date")
    list_filter  = ("borrowed_at", "due_date")
    autocomplete_fields = ("book", "user")
