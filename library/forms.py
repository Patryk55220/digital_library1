from django import forms
from .models import Book, Loan

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = "__all__"
        