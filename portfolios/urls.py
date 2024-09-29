from django.contrib import admin
from django.urls import include, path
from . import views
# from .views import ChatView

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('',views.index,name="index"),
    # path('chat/', ChatView.as_view(), name='chat'),
]