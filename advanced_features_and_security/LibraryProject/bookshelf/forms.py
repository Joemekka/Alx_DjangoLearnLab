from django import forms
from .models import Book


class ExampleForm(forms.ModelForm):
    """
    Example form required for ALX checker.
    """

    class Meta:
        model = Book
        fields = ["title", "author"]
