from rest_framework import routers
from django.urls import path, include
from . import views
from rest_framework.authtoken import views as rest_framework_views
app_name = 'alertupload_rest'

urlpatterns = [
    # Alert POST
    path('images/', views.post_alert, name='post_alert'),

    # Authentication
    path('get_auth_token/', rest_framework_views.obtain_auth_token, name='get_auth_token'),
]