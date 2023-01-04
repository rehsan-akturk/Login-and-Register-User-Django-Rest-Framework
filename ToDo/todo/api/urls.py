from rest_framework import views
from .views import RegisterAPI,  LoginAPI,UserApi,UserRandomApi
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework import renderers


urlpatterns = [
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema-yaml'}
    ), name='swagger-ui'),
    path('openapi.yaml', get_schema_view(
            title="Best API Service",
            renderer_classes=[renderers.OpenAPIRenderer]
        ), name='openapi-schema-yaml'),
    path('openapi.json', get_schema_view(
            title="Best API Service",
            renderer_classes = [renderers.JSONOpenAPIRenderer], 
        ), name='openapi-schema-json'),
    path('users/', UserApi.as_view(), name='getall'),
    path('users/<int:id>/', UserApi.as_view(), name='getid'),
    path('user-random/', UserRandomApi.as_view(), name='get_random'),
    
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall')
]