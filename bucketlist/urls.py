from django.urls import path
from .views import UserList

urlpatterns = [
    path('bucketlist/', UserList.as_view(), name='bucketlist'),
]
