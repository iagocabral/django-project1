# 1 - Iniciando aplicação e subindo o servidor
Configurando o ambiente de desenvolvimento, instalando o Django e colocamos o servidor do nosso projeto no ar pela primeira vez.

## 1) Estabeleça um ambiente virtual dentro do diretório do projeto
Linux/MacOS:
> virtualenv -p python3 venv

Windows:
>python -m virtualenv venv

## 2) Ative o ambiente virtual
Linux/MacOS:
> source venv/bin/activate

Windows:
> source venv/Scripts/activate

## 3) Instale o Django
>pip install django

## 4) Crie o projeto Django
> django-admin startproject setup .

## 5) Rode o servidor pela primeira vez
> python manage.py runserver

### Pronto! Agora você já subiu um servidor Django pela primeira vez.


