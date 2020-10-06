from django.urls import path

from .views import AuthorCreateRestView, AuthorListRestView, AuthorDetailRestView

urlpatterns = [
    path('', AuthorListRestView.as_view(), name='all_author'),
    path("detail/<int:pk>/", AuthorDetailRestView.as_view(), name="update_author"),
    path("create/", AuthorCreateRestView.as_view(), name="create_rest_author"),
]
