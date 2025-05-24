from django import forms
from .models import Book, Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ("first_name", "last_name")

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "author", "year")
    def clean_year(self):
        year = self.cleaned_data["year"]
        if year < 1450 or year > 2100:
            raise forms.ValidationError("Podaj prawidłowy rok wydania.")
        return year
