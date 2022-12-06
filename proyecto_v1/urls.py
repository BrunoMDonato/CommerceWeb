from django.contrib import admin
from django.urls import path, include
from proyecto_app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Inicio, name='Inicio')
]
