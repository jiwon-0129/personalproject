"""maps URL Configuration

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
from django.urls import path
import mad.views
from django.conf import settings 
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.views.generic import ListView, DetailView
from mad.models import *
import account.views

urlpatterns = [
   path('admin/', admin.site.urls),
    path('',mad.views.showmap, name="showmap"),
    path('new/', mad.views.new, name="new"),
    path('create/', mad.views.create, name="create"),
    path("restaurants/<int:restaurants_id>", mad.views.detail, name="detail"),
    path('<int:restaurants_id>/comment', mad.views.add_comment_to_post, name='add_comment_to_post'),
    path('account/login', account.views.login_view, name="login"),
    path('account/logout', account.views.logout_view, name="logout"),
    path('account/register', account.views.register_view, name="register"),
    path('comment/update_comment/restaurants/<int:comment_id>', mad.views.update_comment, name="update_review"),
    path('comment/del_comment/restaurants/<int:comment_id>',mad.views.del_comment, name='del_comment'),
    path('family/restaurants',mad.views.family, name="family"),
    path('friends/restaurants',mad.views.friends, name="friends"),
    path('self/',mad.views.self, name="self"),
    path('lovers/',mad.views.lovers, name="lovers"),
    path('senior',mad.views.senior, name="senior"),
    path('tag/<str:tag>/', mad.views.TaggedObjectLV.as_view(), name='tagged_object_list'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
