from django.urls import path
from . import views

urlpatterns = [

  
    path('genres/', views.GenreCreateListView.as_view(),name='genres_create_list_view'),
    path('genres/<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(),name='genres_update_delete'),

]