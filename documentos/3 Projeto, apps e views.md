# Topico 3 - Projeto, apps e views
 colocamos no ar a nossa primeira página da web personalizada. Pudemos ver como utilizar o HTML dentro do código Python e inserir uma frase simples (ou mesmo um texto complexo) que mostre resultado da página index da aplicação. 

 ## 1) Acesse o arquivo views.py dentro do diretório do app galeria e crie um função responsável por mostrar um HTML da página principal do site;
 >from django.http import HttpResponse<br>
def index(request):<br>
return HttpResponse('texto')

## 2) Crie um novo arquivo chamado urls.py dentro do diretório da aplicação galeria;

<br>

## 3) Crie uma “palheta” de urls dentro do arquivo urls.py (do diretório galeria) que leve à função index;
>from django.contrib import admin<br>
from django.urls import path, include<br>

>urlpatterns = [<br>
    path('admin/', admin.site.urls),<br>
    path('', include('galeria.urls')),<br>
]

### Pronto! Agora, ao subir o servidor, veremos nossa primeira página personalizada com os dizeres: Bem vindo à minha primeira página!!!!

