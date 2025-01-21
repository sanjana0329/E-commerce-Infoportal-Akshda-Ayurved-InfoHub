from core import views
from django.contrib import admin
from django.conf import settings
from django.urls import path,reverse_lazy
from django.conf.urls.static import static

urlpatterns = [
    # FOR MAIN DASHBOARD VIEW
    path('myprofile/', views.MyProfileView.as_view(),name='myprofile'),
    path('contactus/', views.ContactUsView.as_view(),name='contactus'),
    
    path('facial-ubtan/', views.FacialUbtanView.as_view(), name='facial_ubtan'),
    path('kumkumadi-oil/', views.KumkumadiOilView.as_view(), name='kumkumadi_oil'),
    path('peel-off-mask/', views.PeelOfMaskView.as_view(), name='peel_off_mask'),
    path('bentonite-clay-mask/', views.BenetoniteClayMaskView.as_view(), name='bentonite_clay_mask'),
    path('moroccan-clay-mask/', views.MorrocanClayMaskView.as_view(), name='moroccan_clay_mask'),
    
    path('hair-oil/', views.HairOilView.as_view(), name='hair_oil'),
    
    path('privacy-policy/', views.PrivacyPolicyView.as_view(), name='privacy_policy'),
    
    path('about/', views.AboutUsView.as_view(), name='about'),
]
