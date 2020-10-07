from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView
from rest_framework import generics

from authentication.models import CustomUser
from .serializer import CustomUserSerializer


class CustomUserCreateRestView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer


class CustomUserListRestView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class CustomUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
