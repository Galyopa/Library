from django.urls import path

from .views import AuthorViewById, AuthorViewAll,AuthorDeleteView, AuthorCreateView, AuthorUpdateView

urlpatterns = [
    path('<int:pk>/', AuthorViewById.as_view(), name='author_by_id_url'),
    path('', AuthorViewAll.as_view(), name='all_author'),
    path("delete/<int:pk>/", AuthorDeleteView.as_view(), name="delete_author"),
    path("update/<int:pk>/", AuthorUpdateView.as_view(), name="update_author"),
    path("create/", AuthorCreateView.as_view(), name="create_author"),
]
