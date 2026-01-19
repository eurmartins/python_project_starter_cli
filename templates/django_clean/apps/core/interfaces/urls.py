from django.urls import path
from .hello_controller import hello_view

urlpatterns = [
    path('hello/', hello_view, name='hello'),
]