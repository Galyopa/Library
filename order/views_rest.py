from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView
from rest_framework import generics

from order.models import Order
from .serializer import OrderSerializer


class OrderCreateRestView(generics.CreateAPIView):
    serializer_class = OrderSerializer


class OrderListRestView(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
