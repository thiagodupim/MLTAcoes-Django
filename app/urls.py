from django.urls import re_path
from django.conf.urls import include
from app import views

urlpatterns = [
   re_path(r'^api/app$', views.app_list),
   re_path(r'^api/app/(?P<pk>[0-9]+)$', views.app_detail),
   re_path(r'^api/app/published$', views.app_list_published)
]
