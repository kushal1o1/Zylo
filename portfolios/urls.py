from django.contrib import admin
from django.urls import include, path
from . import views
from .views import update_user_info

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('create/',views.index,name="index"),
    path('',views.home,name="home"),
    
    
    # path('chat/', ChatView.as_view(), name='chat_view'),
     path('update_user_info/', update_user_info, name='update_name'),
]