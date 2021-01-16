
from django.contrib import admin
from django.urls import path
from Medium.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name = 'home'),
    path('all_blogs/', AllBlogs, name='all_blogs'),
]
