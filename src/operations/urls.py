from graphene_django.views import GraphQLView
from django.urls import path
from .schemas import schema


urlpatterns = (
    path(route='graphql', view=GraphQLView.as_view(graphiql=True, schema=schema)),
)

