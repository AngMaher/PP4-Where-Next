from . import views
from django.urls import path
from .views import UserView


urlpatterns = [
    path('bucketlist/', UserList.as_view(), name='bucketlist'),
]
