# alpinejs-django-ninja-crud

CRUD com AlpineJS e Django Ninja.

Este repositório apresenta um sistema CRUD (Create, Read, Update, Delete) implementado utilizando AlpineJS e Django Ninja. AlpineJS é um framework JavaScript leve e reativo, enquanto Django Ninja é um conjunto de ferramentas para construir APIs rápidas com Django.

## Tecnologias Utilizadas:

* **AlpineJS:** Framework JavaScript minimalista que facilita a criação de interfaces reativas e dinâmicas no lado do cliente.

* **Django Ninja:** Um conjunto poderoso de ferramentas para construir APIs rápidas usando Django, proporcionando uma integração suave com o backend.

* **Pico CSS:** Um framework CSS simples e eficiente.


## Objetivos:

* Mostrar recursos e funcionalidades do AlpineJS.
* Criar um CRUD com Django Ninja.

![](img/mockup.png)

## Este projeto foi feito com:

* [Python 3.11.7](https://www.python.org/)
* [Django 5.0](https://www.djangoproject.com/)
* [Django-Ninja 1.0.1](https://django-ninja.rest-framework.com/)
* [AlpineJS](https://alpinejs.dev/)
* [Pico CSS](https://picocss.com/)


## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/alpinejs-django-ninja-crud.git
cd alpinejs-django-ninja-crud

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python contrib/env_gen.py

python manage.py migrate
python manage.py createsuperuser

python manage.py runserver
```