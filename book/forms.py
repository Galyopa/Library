from django import forms

from author.models import Author
from .models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['name', 'description', 'authors']

        labels = {
            'name': 'Enter book name',
            'description': 'Enter description',
            'authors': 'Please select author',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'authors': forms.SelectMultiple(attrs={'class': 'form-control'})
        }
