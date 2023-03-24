from . import views
from django.urls import path


urlpatterns = [
    path('', views.BlogPosts.as_view(), name='home'),
    path('<slug:slug>/', views.PostContent.as_view(), name='post_content'),
]