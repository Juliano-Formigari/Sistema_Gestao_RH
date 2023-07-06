# Sistema_Gestao_RH

    Sistema de gestão RH open source, desenvolvido no curso avancado - Gregory Pacheco
    [Curso avançado aplicações Django](https://www.udemy.com/course/desenvolvimento-avancado-de-aplicacoes-corporativas-c-django/?kw=desenvolvimento+avan%C3%A7ado+de+aplica&src=sac)

    Conceitos abordados no curso:
        Arquitetura Multi-tenant;
        Arquitetura Multi-database;
        Arquitetura Multi-idiomas;
        Arquitetura Multi-location;
        Celery para tarefas assincronas;
        HTTP Stream;
        Interação com servidor via Ajax;
        Interações do servidor com FrontEnd via Websocket;
        Django messages framework;
        Expondo uma REST API;

    Requisitos do sistema:
        Registro de todos os funcionários da empresa;
        Controle de departamentos;
        Controle de férias;
        Banco de horas;
        Registro de documentos (Atestados médicos, contratos, scanner de documentos)
    Relatórios:
        Listagem de funcionários;
        Listagem de funcionários por departamento;
        Listagem de funcionários de férias;
        Relatório de banco de dados;


# Comandos utilizados no curso
    python -m venv venv;
    source venv/Scripts/activate;
    pip install Django;
    django-admin startproject nomeDoProjeto .;
    python manage.py runserver;
    python manage.py migrate;
    python manage.py createsuperuser;
    python manage.py startapp nomeDoApp;
    pip install django-bootstrap-v5
    pip freeze > requirements.txt
    python manage.py shell
    pip install django-bootstrap-form
    python manage.py collectstatic - Comando utilizado pelo django para copiar todos os arquivos estáticos para somente um diretório. Este comando é utilizado no momento em que é feito o deploy.

    Juliano - Admin123
    Greg - Greg123Greg

# Anotações e dicas importantes
    Sempre que mover um 'app' para um subdiretório após a instalação, acrescentar no campo 'name' do arquivo 'apps.py' o diretório principal na frente do nome do app;

    Dentro de core foi criado um subdiretório "core", para separar caso tenha outra template com o mesmo nome e não correr o
    risco de pegar a primeira;