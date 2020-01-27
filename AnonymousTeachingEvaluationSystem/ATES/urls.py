from ATES import views
from django.urls import re_path
urlpatterns = [
        re_path(r'^$', views.homepage),
        re_path(r'^searchinformation', views.searchinformation),
    ]