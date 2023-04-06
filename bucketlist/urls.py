from django.urls import path
from .views import UserList, AddListItem, UpdateListItem

urlpatterns = [
    path('bucketlist/', UserList.as_view(), name='bucketlist'),
    path('add_list_item/', AddListItem.as_view(), name="add_list_item"),
    path('update_list_item/<int:pk>', UpdateListItem.as_view(), name="update_list_item"),
]
