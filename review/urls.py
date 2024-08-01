from django.urls import path
from . import views

urlpatterns = [

    path('review/', views.ListCreateReview.as_view(),name='review_create_list_view'),
    path('review/<int:pk>/', views.UpdateDeleteReview.as_view(),name='review_update_delete'),
]
