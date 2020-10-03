from django.urls import path
from .views import BooksListViewByAuthor, BooksViewById, BooksViewAll
from . import views

urlpatterns = [
    path('authors_book/<authors>/', BooksListViewByAuthor.as_view(), name='books_list_url'),
    path('<int:pk>/', BooksViewById.as_view(), name='book_by_id_url'),
    path('', BooksViewAll.as_view(), name='all_books'),
    path('create', views.create_book, name="book_create"),
    path('update', views.update_book, name="book_update"),
    path('delete', views.delete_book, name="book_delete")
]
