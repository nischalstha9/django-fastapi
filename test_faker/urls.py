
from django.urls import path, include
from .views import PersonListAPIView

urlpatterns = [
    path('',PersonListAPIView.as_view()),
]
