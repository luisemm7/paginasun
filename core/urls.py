from django.urls import path
from .views import home1, about1, politica1

urlpatterns = [
    path('', home1, name="home"),
    path('about/', about1, name="about"),
    path('politica/', politica1, name="politica"),
]
