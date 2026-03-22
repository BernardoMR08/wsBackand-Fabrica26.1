from django.contrib import admin
from django.urls import path
from .views import home
from django.urls import path, include



urlpatterns = [
    path('', home, name='home'),
     path('admin/', admin.site.urls),
    path('', include('finance.urls')),
]