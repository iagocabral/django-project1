# Topico 4 - Arquivos estáticos
Implementamos um novo template no site que estamos desenvolvendo. Inserimos arquivos estáticos e reconfiguramos o arquivo settings.py.

## 1) Criamos uma página chamada templatesno diretório raiz do nosso projeto;
<br>

## 2) Dentro da pasta templates, vamos criar um diretório para cada app que temos. Sendo assim, criamos um diretório chamado galeria;
<br>

## 3) Criamos um arquivo chamado index.html dentro do diretório galeria. Ele será a página principal do site;
<br>

## 4) Inserimos no arquivo index.html o código disponibilizado nesta página;
<br>

## 5) Indicamos no arquivo settings.py no diretório setup que os templates do projeto devem ser utilizados através do diretório templates;
>….
TEMPLATES = [<br>
    {<br>
        'BACKEND': 'django.template.backends.django.DjangoTemplates',<br>
        'DIRS': [os.path.join(BASE_DIR, 'templates')],<br>
        'APP_DIRS': True,<br>
….

## 6) Alteramos o arquivo views.py do app galeria para considerar essa mudança;
>from django.shortcuts import render<br>

>def index(request):<br>
    return render(request, ‘galeria/index.html’)<br>

## 7) Incluímos os diretórios de arquivos estáticos styles e assets, que podem ser baixados neste link, dentro do diretório static presente no diretório setup;
<br>

## 8) Indicamos no arquivo settings.py no diretório setup que os arquivos estáticos do projeto devem ser utilizados através do diretório static; 
>STATIC_URL = 'static/'

>STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'setup/static')
]

>STATIC_ROOT = os.path.join(BASE_DIR, 'static')

## 9) Rodamos o seguinte comando para fazer o django reconhecer os arquivos estáticos do projeto;
>python manage.py collectstatic

## 10) Dentro do arquivo index.html inserimos a seguinte linha de código em Python que indicará que a página deve carregar arquivos estáticos;
>{% load static %}

## 11) Mudamos a referência dos arquivos estáticos dentro do arquivo index.html para comunicar a localização dos arquivos estáticos através de código python;
>{% load static %}<br>

     <link rel="stylesheet" href="{% static '/styles/style.css' %}">
