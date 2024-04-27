from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registrationPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('contactForm/',views.contactForm,name='contactForm'),
    path('userHome/',views.userHome,name='userHome'),
    path('logoutUser/',views.logoutUser,name='logoutUser'),
    path('forgotPass/',views.forgotPass,name='forgotPass'),
    path('createSurvey/',views.createSurvey,name='createSurvey'),
    path('addQuestions/<int:surveyID>',views.addQuestions,name='addQuestions'),
    path('closeSurvey/<int:surveyID>',views.closeSurvey,name='closeSurvey'),
    path('openSurvey/<int:surveyID>',views.openSurvey,name='openSurvey'),
    path('viewResponses/<int:surveyID>',views.viewResponses,name="viewResponses"),
    path('reviewSurvey/<int:surveyID>',views.reviewSurvey,name='reviewSurvey'),
    path('fillSurvey/<int:surveyID>',views.fillSurvey,name='fillSurvey'),
]