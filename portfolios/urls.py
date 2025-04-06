from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import update_user_info,update_images,update_background_image,delete_background_image

urlpatterns = [
    path('', views.main_page, name='MainPage'),
    path('create/',views.home,name="home"),
    path('update_user_info/', update_user_info, name='update_user_info'),
    path('update_images/', update_images, name='update_images'),
    
    # Url for updating background image
    path('update_background_image/', update_background_image, name='update_background_image'),
    path('delete_background_image/', delete_background_image, name='delete_background_image'),

    # Urls for handling highlights
    path('highlights/delete/<int:highlight_id>/', views.delete_highlight, name='delete_highlight'),  # Delete highlight


    path('sections/delete/<int:section_id>/', views.delete_section, name='delete_section'),
    path('delete-section-data/<int:data_id>/', views.delete_section_data, name='delete_section_data'),
    path('get-code-snippet/', views.get_code_snippet, name='get_code_snippet'),
    path("NotFound/",views.not_found,name="NotFound"),
    path('<str:userUrl>/',views.index,name="index"),
    
    
  

     
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)