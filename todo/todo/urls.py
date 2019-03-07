from django.contrib import admin
from django.urls import path,include
from todo_list import views

urlpatterns = [
    path('',include('todo_list.urls')),
    path('admin/', admin.site.urls),
]
