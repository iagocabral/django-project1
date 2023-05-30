#Criei esse arquivo para isolar as urls da galeria
from django.urls import path
from galeria.views import index, imagem #IMPORTANDO AS VIEWS

urlpatterns = [
    path('', index, name='index'), #tag name para referenciar no html
    path('imagem/', imagem, name='imagem'), #CAMINHO PARA imagem/ retorna imagem
]
