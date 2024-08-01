from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalPermission


class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated, GlobalPermission)


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticated, GlobalPermission)
