from . import views
from bucketlist.views import UserList
from django.urls import path, include


urlpatterns = [
    path('', views.BlogPosts.as_view(), name='home'),
    path('<slug:slug>/', views.PostContent.as_view(), name='post_content'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('bucketlist/', UserList.as_view(), name='bucketlist'),
]
