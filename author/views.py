from abc import ABC

from django.http import Http404
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView, CreateView

from authentication.models import CustomUser
from author.forms import AuthorForm
from author.models import Author


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
    page_title = "Create Author"
    model = Author
    form_class = AuthorForm
    # permission_required = "add_author"

    template_name = 'author_form.html'
    success_url = '/author'
    # def get_success_url(self):
    #     return reverse("authors:author_by_id_url", args=(self.object.pk,))

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


def delete_author(request, id):
    if not request.user.is_authenticated:
        messages.info(request, "Log in first!")
        return redirect("authorise")
    if not CustomUser.get_by_email(request.user.email).role == 1:
        messages.info(request, "You don`t have permission!")
        return redirect("home")
    Author.delete_by_id(id)
    return redirect("all_author")
