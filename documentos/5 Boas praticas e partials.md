# Topico 5 - Boas praticas e partials
 aprendemos o que é a prática DRY (Don't Repeat Yourself - Não se repita, numa tradução livre) e a colocamos em prática diminuindo as repetições de código presentes nos arquivos de template do projeto.

## 1) Vamos implementar o método DRY (Don't Repeat Yourself - Não se repita) criando um arquivo chamado base.html dentro do diretório galeria em templates;
<br>

## 2) Inserimos no arquivo base.html os trechos de código que se repetem em index.html e imagem.html;
<br>
    
## 3) Também inserimos no meio do arquivo base.html um indicativo de onde deve ser inserido o bloco de conteúdo que se diferencia em index.html e imagem.html;

        {% load static %}
    <!DOCTYPE html>
    <html lang="pt-br">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Alura Space</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="{% static '/styles/style.css' %}">
    </head>

    <body>
        {% block content %}{% endblock %}
    </body>
    </html>

## 4) Colocamos no início dos arquivos index.html e imagem.html um código Python que indica a importação do código em base.html, bem como, o início e o final do bloco de conteúdo de cada uma;
        {% extends 'galeria/base.html' %}
    {% load static %}
    {% block content %}

    ....

    {% endblock %}

## 5) Melhoramos ainda mais a prática do DRY! Criamos um novo diretório dentro de templates/galeria chamado partials;
<br>

## 6) Dentro desse novo diretório partials, criamos um novo arquivo chamado _footer.html;
<br>

## 7) Inserimos dentro de _footer.html o código de imagem.html e index.html correspondente;
    {% load static %}
    <footer class="rodape">
        <div class="rodape__icones">
            <a href="https://twitter.com/AluraOnline" target=”_blank” >
                <img src="{% static '/assets/ícones/1x/twitter.png' %}" alt="ícone twitter">
            </a>
            <a href="https://www.instagram.com/aluraonline/" target=”_blank” >
                <img src="{% static '/assets/ícones/1x/instagram.png' %}" alt="ícone instagram">
            </a>
        </div>
        <p class="rodape__texto">Desenvolvido por Alura</p>
    </footer>

## 8) Excluímos o código correspondente ao footer em imagem.html e index.html;
<br>

## 9) Adicionamos em `base.html um novo "bloco de código";
        {% load static %}
    <!DOCTYPE html>
    <html lang="pt-br">

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Alura Space</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="{% static '/styles/style.css' %}">
    </head>

    <body>
        {% block content %}{% endblock %}
        {% include 'galeria/partials/_footer.html' %}
    </body>

    </html>


### Então temos um código mais atualizado em boas práticas de desenvolvimento. Porém, ainda podemos aplicar ainda mais a prática DRY
- Aprendemos sobre a prática DRY (Don’t Repeat Yourself - Não se repita) e a colocamos em ação criando uma arquivo chamado base.html que irá conter código repetido em diversos templates para evitar essa repetição;
- Utilizamos o artifício das Partials para seguir com a prática DRY, evitando mais repetição de código e tornando mais eficiente a escalabilidade do site.

    
