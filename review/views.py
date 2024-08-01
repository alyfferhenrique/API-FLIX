from rest_framework import generics
from review.models import Review
from review.serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalPermission

class ListCreateReview(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated, GlobalPermission)

class UpdateDeleteReview(generics.RetrieveDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated, GlobalPermission)