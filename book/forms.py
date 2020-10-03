from django.forms import ModelForm
from .models import Book

class CreateForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'count']


class UpdateForm(ModelForm):
    class Meta:
        model = Book
        fields = ['id','name', 'description', 'count']