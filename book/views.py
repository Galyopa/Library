from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, CreateView

from .forms import BookForm

from author.models import Author
from book.models import Book


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


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    permission_required = "add_book"
    template_name = 'create_book.html'
    success_url = '/book'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


def update_book(request):
    if request.method == 'GET':
        id = request.GET["id"]
        book = Book.get_by_id(id)
        return render(request, 'update_book.html', {'book': book})

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
