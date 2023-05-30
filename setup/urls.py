from django.contrib import admin
from django.urls import path, include #Adicionei o include para a boa pratica de isolar as galerias
#criei o galeria > urls.py para isolar todas as urls da galeria

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
]
