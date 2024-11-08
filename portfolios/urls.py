from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import update_user_info,update_images

urlpatterns = [
    
    path('create/',views.home,name="home"),
    path('update_user_info/', update_user_info, name='update_user_info'),
    path('update_images/', update_images, name='update_images'),

    
    path('highlights/', views.highlight_list, name='highlight_list'),  # List and create/edit highlights
    path('highlights/delete/<int:highlight_id>/', views.delete_highlight, name='delete_highlight'),  # Delete highlight

    path('sections/delete/<int:section_id>/', views.delete_section, name='delete_section'),
    path('delete-section-data/<int:data_id>/', views.delete_section_data, name='delete_section_data'),

    path("NotFound/",views.NotFound,name="NotFound"),
    path('<str:userUrl>/',views.index,name="index"),
    
  

    
    
    # path('chat/', ChatView.as_view(), name='chat_view'),
     
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)