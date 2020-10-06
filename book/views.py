from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView
from rest_framework import generics

from .forms import CreateForm

from author.models import Author
from book.models import Book
from .serializer import BookSerializer


class BooksListViewByAuthor(ListView):
    model = Book
    template_name = 'books.html'
    context_object_name = 'books'
    paginate_by = 10

    def get_queryset(self):
        self.authors = get_object_or_404(Author, name=self.kwargs['authors'])
        return Book.objects.filter(authors=self.authors)


class BooksViewById(ListView):
    model = Book
    template_name = 'books.html'
    context_object_name = 'books'
    paginate_by = 10

    def get_queryset(self):
        try:
            return Book.objects.filter(pk=self.kwargs['pk'])
        except Book.DoesNotExist:
            raise Http404("No Books matches the given query.")


class BooksViewAll(ListView):
    model = Book
    template_name = 'books.html'
    context_object_name = 'books'
    paginate_by = 10
    queryset = Book.objects.all()


def create_book(request, template_name='create.html'):
    form = CreateForm(request.POST or None)
    if form.is_valid():
        name = request.POST.get("name")
        description = request.POST.get("description")
        count = request.POST.get("count")
        author = Author.get_by_id(request.POST.get("author_id"))
        Book.create(name, description, count, authors=[author])
        return redirect('/book')
    authors = Author.get_all()
    return render(request, template_name, {'form': form, 'authors': authors})


def update_book(request):
    if request.method == 'GET':
        id = request.GET["id"]
        book = Book.get_by_id(id)
        return render(request, 'update.html', {'book': book})

    if request.method == 'POST':
        id = request.POST.get("id")
        book = Book.get_by_id(id)
        book.name = request.POST.get("name")
        book.description = request.POST.get("description")
        book.count = request.POST.get("count")
        book.save()
        return redirect('/book')


def delete_book(request):
    id = request.GET["id"]
    Book.delete_by_id(id)
    return redirect('/book')


class BookCreateRestView(generics.CreateAPIView):
    serializer_class = BookSerializer


class BookListRestView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
