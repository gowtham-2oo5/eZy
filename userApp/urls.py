from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='user_index'),
    path('create_form',views.create_form,name='create_form'),
    path('save_user',views.save_user,name='save_user'),
    path('manage_forms',views.manage_forms,name='manage_forms'),
    path('manage_profile',views.manage_profile,name='manage_profile'),
    path('logout',views.logout,name='logout'),
    path('user_dashboard',views.refresh_user,name='refresh_user'),
    path('user_grievances',views.user_grievances,name='user_grievances'),
    path('update_profile',views.update_profile,name='update_profile'),
    path('initialize_form',views.initialize_form,name='initialize_form'),
    path('add_questions',views.add_questions,name='add_questions'),
]