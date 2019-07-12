from django.urls import path
from django.conf.urls import url
from graphene_django.views import GraphQLView

from . import views
from BigDickServer.schema import schema

urlpatterns = [
    url(r'^graphql$', GraphQLView.as_view(graphiql=True, schema = schema)),
    path('new_recipe', views.create_recipe, name='create recipe'),
]