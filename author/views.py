from abc import ABC

from django.http import Http404
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework import generics

from author.forms import AuthorForm
from author.models import Author
from author.serializer import AuthorSerializer


class AbstractAuthorView(ABC):
    odel = Author
    template_name = 'author.html'
    context_object_name = 'authors'
    paginate_by = 10


class AuthorViewById(AbstractAuthorView, ListView):

    def get_queryset(self):
        try:
            return Author.objects.filter(pk=self.kwargs['pk'])
        except Author.DoesNotExist:
            raise Http404("No Books matches the given query.")


class AuthorViewAll(AbstractAuthorView, ListView):
    queryset = Author.objects.all()


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    permission_required = "add_author"
    template_name = 'author_form.html'
    success_url = '/author'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AuthorUpdateView(UpdateView):
    permission_required = "change_author"
    model = Author
    form_class = AuthorForm
    template_name = 'author_form_update.html'
    success_url = '/author'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("author_by_id_url", args=(self.object.pk,))


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = '/author'
    permission_required = "delete_author"
    template_name = 'author_confirm_delete.html'


class AuthorCreateRestView(generics.CreateAPIView):
    serializer_class = AuthorSerializer


class AuthorListRestView(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorDetailRestView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
