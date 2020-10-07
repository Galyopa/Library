from rest_framework import generics

from author.models import Author
from author.serializer import AuthorSerializer


class AuthorCreateRestView(generics.CreateAPIView):
    serializer_class = AuthorSerializer


class AuthorListRestView(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorDetailRestView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
