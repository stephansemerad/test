from django.contrib import admin
from django.urls import path, include
from app import views
from . import settings

# here we have the redirect to the different applications that you have created
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]
