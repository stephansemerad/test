from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.index),
    # path('shorten/', views.get_form, name='urlform'),
    # path('<short_url>/', views.redirect_short_url, name='redirectpath'),
]
