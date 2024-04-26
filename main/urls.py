from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registrationPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('contactForm/',views.contactForm,name='contactForm'),
    path('userHome/',views.userHome,name='userHome'),
    path('logoutUser/',views.logoutUser,name='logoutUser'),
    path('forgotPass/',views.forgotPass,name='forgotPass')
]