from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.CarListView.as_view()),
    path('cars/<int:pk>/', views.CarDetailView.as_view()),
]
