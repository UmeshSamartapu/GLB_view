from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('upload/', views.upload_model, name='upload'),
    path('mobile/', views.mobile_view, name='mobile'),
    path('laptop_ar/', views.laptop_view, name='laptop'),
]