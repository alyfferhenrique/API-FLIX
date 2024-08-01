from django.urls import path
from . import views

urlpatterns = [

    path('movies/', views.MovieCreateListView.as_view(), name='movies_create_list_view'),
    path('movies/<int:pk>/', views.MovieRetrieveUpdateDestroyView.as_view(),name='movies_update_delete'),
    path('movies/stats/', views.MovieStatsView.as_view(), name='movie-stats-view'),
]
