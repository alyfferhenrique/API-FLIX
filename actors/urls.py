from django.urls import path
from . import views

urlpatterns = [

path('actors/', views.ActorCreateListView.as_view(),name='actors_create_list_view'),
path('actors/<int:pk>/', views.ActorRetrieveUpdateDestroyView.as_view(),name='actors_update_delete'),

]
