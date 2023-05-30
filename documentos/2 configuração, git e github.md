# Topico 2 - Configurações, Git e Github
Garantimos uma maior segurança na aplicação através da utilização do pacote python-dotenv.<br>

Aprendemos que dados sensíveis como a SECRET_KEY, devem ser armazenados em em um arquivo específico ao ambiente atual de desenvolvimento.

## 1)  Instale o pacote python-dotenv
>pip install python-dotenv

<br>

## 2) Crie um novo arquivo chamado .env no diretório raiz da aplicação para armazenar a SECRET_KEY
> SECRET_KEY=<chave aleatória>

<br>

## 3) Importe os pacotes python-dotenv e os no arquivo settings.py
>from pathlib import os<br>
from dotenv import load_dotenv

## 4) Importe a SECRET_KEY do arquivo .env e coloque dentro da variável SECRET_KEY no arquivo settings.py
>oad_dotenv()<br>
SECRET_KEY = str(os.getenv('SECRET_KEY'))

<br>

## 5) Gere um arquivo .gitignore no diretório raiz do projeto e inclua o arquivo .env como conteúdo 
<br>


### Pronto! Assim deixamos o projeto mais seguro, impedindo que dados sensíveis fiquem à mercê de commits descuidados.