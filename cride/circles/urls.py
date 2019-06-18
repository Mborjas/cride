"""Circles URLs."""

# Django
from django.urls import include, path


# Views
from cride.circles.views import list_circles

urlpatterns = [
    path('circles/', list_circles)
]

