from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usersapp/', include('usersapp.urls')),
    path('', views.homepage),
    path('despre', views.despre),
    path('contact', views.contact),
]