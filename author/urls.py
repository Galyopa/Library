from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import AuthorViewById, AuthorViewAll,AuthorDeleteView, AuthorCreateView, AuthorUpdateView

urlpatterns = [
    path('<int:pk>/', AuthorViewById.as_view(), name='author_by_id_url'),
    path('', AuthorViewAll.as_view(), name='all_author'),
    path("delete/<int:pk>/", login_required(AuthorDeleteView.as_view()), name="delete_author"),
    path("update/<int:pk>/", login_required(AuthorUpdateView.as_view()), name="update_author"),
    path("create/", login_required(AuthorCreateView.as_view()), name="create_author"),
]
