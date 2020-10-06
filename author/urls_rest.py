from django.urls import path

from .views import AuthorCreateRestView, AuthorListRestView, AuthorDetailRestView

urlpatterns = [
    path('', AuthorListRestView.as_view(), name='all_author_rest'),
    path("detail/<int:pk>/", AuthorDetailRestView.as_view(), name="update_delete_rest_author"),
    path("create/", AuthorCreateRestView.as_view(), name="create_rest_author"),
]
