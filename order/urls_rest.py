from django.urls import path
from .views_rest import OrderCreateRestView, OrderListRestView, OrderDetailView

urlpatterns = [
    path("", OrderListRestView.as_view(), name="all_orders_rest"),
    path("create", OrderCreateRestView.as_view(), name="order_create_rest"),
    path(
        "detail/<int:pk>/", OrderDetailView.as_view(), name="order_update_delete_rest"
    ),
]
