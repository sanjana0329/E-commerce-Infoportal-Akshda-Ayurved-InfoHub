from core import views
from django.contrib import admin
from django.conf import settings
from django.urls import path,reverse_lazy
from django.conf.urls.static import static

urlpatterns = [
    # FOR MAIN DASHBOARD VIEW
    path('myprofile/', views.MyProfileView.as_view(),name='myprofile'),
     
]
