from . import views
from .views import CategoryView, AboutView
from bucketlist.views import UserList
from django.urls import path, include


urlpatterns = [
    path('', views.BlogPosts.as_view(), name='home'),
    path('about/', AboutView, name='about'),
    path('<slug:slug>/', views.PostContent.as_view(), name='post_content'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('category/<int:cats>', CategoryView, name='category'),
]
