"""wherenext URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('travelblog.urls'), name='travelblog_urls'),
    path('accounts/', include('allauth.urls')),
    path('bucketlist/', include('bucketlist.urls'), name='bucketlist_urls'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = "travelblog.views.handler_404"
handler404 = "travelblog.views.handler_403"
handler404 = "travelblog.views.handler_500"
