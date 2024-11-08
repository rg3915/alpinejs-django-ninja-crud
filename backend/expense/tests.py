from http import HTTPStatus

import pytest

from .models import Expense


@pytest.mark.django_db
def test_atualiza_despesa_sem_person(client):
    Expense.objects.create(description='Livro', value=90)

    payload = dict(
        description='Livro de Python',
        value=50
    )

    response = client.patch('/api/v1/expenses/1', payload, content_type='application/json')

    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
def test_atualiza_despesa_sem_person_e_sem_value(client):
    Expense.objects.create(description='Livro', value=90)

    payload = dict(
        description='Livro de Python'
    )

    response = client.patch('/api/v1/expenses/1', payload, content_type='application/json')

    assert response.status_code == HTTPStatus.OK
