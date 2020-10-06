from django.urls import path
from .views import BookCreateRestView, BookListRestView, BookDetailView

urlpatterns = [
    path('', BookListRestView.as_view(), name='all_books_rest'),
    path('create', BookCreateRestView.as_view(), name="book_create_rest"),
    path('detail/<int:pk>/', BookDetailView.as_view(), name="book_update_delete_rest"),
]
