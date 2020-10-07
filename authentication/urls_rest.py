from django.urls import path
from .views_rest import (
    CustomUserCreateRestView,
    CustomUserListRestView,
    CustomUserDetailView,
)

urlpatterns = [
    path("", CustomUserListRestView.as_view(), name="all_custom_users_rest"),
    path("create", CustomUserCreateRestView.as_view(), name="custom_user_create_rest"),
    path(
        "detail/<int:pk>/",
        CustomUserDetailView.as_view(),
        name="custom_user_update_delete_rest",
    ),
]
