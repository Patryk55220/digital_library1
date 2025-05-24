from django import forms
from .models import Book, Loan


class BookForm(forms.ModelForm):
    class Meta:
        model  = Book
        fields = ("title", "author", "year")


class LoanForm(forms.ModelForm):
    class Meta:
        model  = Loan
        fields = ("due_date",)
        widgets = {"due_date": forms.DateTimeInput(attrs={"type": "datetime-local"})}
