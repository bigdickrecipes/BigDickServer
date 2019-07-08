from django.urls import path

from . import views

urlpatterns = [
    path('new_recipe', views.create_recipe, name='create recipe'),
]