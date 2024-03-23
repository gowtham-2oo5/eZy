from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('indexApp.urls')),
    path('auth/',include('authApp.urls')),
    path('auth/',include('django.contrib.auth.urls')),
    path('ezy/',include('userApp.urls'))
]
admin.site.site_header = 'eSurvey Platform'
admin.site.site_title = 'eZy'
admin.site.site_url = 'http://localhost:8000/'