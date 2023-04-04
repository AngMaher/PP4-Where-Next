from .views import UserList
from django.urls import path


urlpatterns = [
    path('bucketlist/', UserList.as_view(), name='bucketlist'),
]
