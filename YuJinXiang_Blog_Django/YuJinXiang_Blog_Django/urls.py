"""
URL configuration for YuJinXiang_Blog_Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('post/', post_view, name='post'),
    path('post_edit/<int:post_id>/', post_edit_view, name='postedit'),
    path('detail/<int:post_id>', detail_view, name='detail'),
    path('postdelete/<int:post_id>/', post_delete_view, name='postdelete'),
    path('friend/', friend_view, name='friend'),
    path('resource/', resource_view, name='resource'),
    path('test/', create_post)
]
