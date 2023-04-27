from django.urls import path
from .views import UserList, AddListItem, UpdateListItem, DeleteListItem, StorePlanning, UpdatePlan  # noqa


urlpatterns = [
    path('bucketlist/', UserList.as_view(), name='bucketlist'),
    path('add_list_item/', AddListItem.as_view(), name="add_list_item"),
    path('update_list_item/<int:pk>', UpdateListItem.as_view(), name="update_list_item"),  # noqa
    path('delete_list_item/<item_id>', DeleteListItem, name="delete_list_item"),  # noqa
    path('store_planning/<int:pk>', StorePlanning.as_view(), name="store_planning"),  # noqa
    path('update_planning/<int:pk>', UpdatePlan.as_view(), name="update_planning"),  # noqa
]
