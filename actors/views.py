
from rest_framework import generics
from actors.models import Actor
from actors.serializers import ActorSerializer 
from rest_framework.permissions import IsAuthenticated 
from app.permissions import GlobalPermission


class ActorCreateListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (IsAuthenticated, GlobalPermission)

class ActorRetrieveUpdateDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (IsAuthenticated, GlobalPermission)