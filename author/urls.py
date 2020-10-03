from django.urls import path

from .views import AuthorViewById, AuthorViewAll, delete_author, AuthorCreateView

# app_name = "authors"

urlpatterns = [
    path('<int:pk>/', AuthorViewById.as_view(), name='author_by_id_url'),
    path('', AuthorViewAll.as_view(), name='all_author'),
    path("delete/<int:id>/", delete_author, name="delete_author"),
    # path("update/<int:id>/", views.register, name="update"),
    path("create/", AuthorCreateView.as_view(), name="create"),
]
