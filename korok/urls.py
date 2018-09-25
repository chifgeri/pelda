from django.urls import path

from . import views

urlpatterns = [
    path('hallgato/', views.HallgatoListView.as_view()),
    path('hallgato/<slug:pk>/', views.HallgatoDetailView.as_view()),
    path('korok/', views.KorListView.as_view()),
]
