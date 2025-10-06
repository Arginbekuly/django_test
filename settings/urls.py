from django.contrib import admin
from django.urls import path
from apps.tasks.views import welcome
from apps.tasks.views import users,city_time,counter_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',welcome,name = 'index'),
    path('users/', users,name = 'users_list'),
    path('city_time/', city_time,name = 'city_time'),
    path('cnt/', counter_view, name='counter'),
]