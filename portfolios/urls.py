from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import update_user_info,update_images

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path("NotFound/",views.NotFound,name="NotFound"),
    path('<str:userUrl>/',views.index,name="index"),
    path('create/',views.home,name="home"),

    
    
    # path('chat/', ChatView.as_view(), name='chat_view'),
     path('update_user_info/', update_user_info, name='update_user_info'),
     path('update_images/', update_images, name='update_images'),
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)