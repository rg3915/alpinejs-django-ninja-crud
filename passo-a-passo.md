# Passo a passo

## Criando o projeto

```
git clone https://github.com/rg3915/alpinejs-django-ninja-crud.git
cd alpinejs-django-ninja-crud

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python contrib/env_gen.py

python manage.py migrate
```

### Criando os arquivos

```
touch backend/api.py

touch backend/core/urls.py

touch backend/expense/forms.py
touch backend/expense/urls.py
touch backend/expense/api.py

mkdir -p backend/core/static/css
touch backend/core/static/css/custom.css

mkdir -p backend/core/static/js
touch backend/core/static/js/expense.js

mkdir -p backend/core/templates/core
touch backend/core/templates/base.html
touch backend/core/templates/core/index.html

mkdir -p backend/expense/templates/expense
touch backend/expense/templates/expense/expense.html
```


Comando para inserir dados pelo shell_plus:

```python
from datetime import date
expenses_data = [
    {"description": "Tenis", "value": 150.75, "date_payment": date(2024, 1, 2)},
    {"description": "Ventilador", "value": 80.50, "date_payment": date(2024, 1, 5)},
    {"description": "Internet", "value": 120.00, "date_payment": date(2024, 1, 8)},
    {"description": "Almoço", "value": 35.25, "date_payment": date(2024, 1, 12)},
    {"description": "Gasolina", "value": 40.00, "date_payment": date(2024, 1, 15)},
    {"description": "Cinema", "value": 45.50, "date_payment": date(2024, 1, 18)},
    {"description": "Pipoca", "value": 60, "date_payment": date(2024, 1, 30)},
    {"description": "Taxi", "value": 80.00, "date_payment": date(2024, 1, 22)},
    {"description": "Sorvete", "value": 4.75, "date_payment": date(2024, 1, 25)},
    {"description": "Café", "value": 8.20, "date_payment": date(2024, 1, 28)},
]

for expense in expenses_data:
    Expense.objects.create(
        description=expense['description'],
        value=expense['value'],
        date_payment=expense['date_payment'],
    )
```



```python
# backend/api.py
from ninja import NinjaAPI
from ninja.security import django_auth

api = NinjaAPI(auth=[django_auth])

api.add_router('', 'backend.expense.api.router')
```

Mostrar backend/core/urls.py
Mostrar backend/expense/urls.py

```python
# backend/expense/forms.py
from django import forms

from .models import Expense


class ExpenseForm(forms.ModelForm):
    date_payment = forms.DateField(
        label='Data',
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
            },
        ),
        input_formats=('%Y-%m-%d',),
    )

    class Meta:
        model = Expense
        fields = (
            'description',
            'value',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['value'].widget.attrs['min'] = 0

        for field_name, field in self.fields.items():
            field.widget.attrs['x-model'] = f'editItem.{field_name}'
```

```python
# backend/expense/models.py
from django.db import models
from datetime import datetime


class Expense(models.Model):
    ...

    def date_payment_display(self):
        if self.date_payment:
            date_str = self.date_payment.isoformat()
            iso_date = datetime.fromisoformat(date_str)
            return iso_date.strftime("%d/%m/%Y")
```


```python
# backend/expense/api.py
ExpenseSchema = create_schema(Expense, custom_fields=(
    ('date_payment_display', str, None),
))


class ExpenseCreateSchema(ModelSchema):
    class Meta:
        model = Expense
        fields = (
            'description',
            'value',
            'date_payment',
        )


@router.get('expenses', response=list[ExpenseSchema])
def list_expense(request):
    return Expense.objects.all()


@router.get('expenses/{pk}', response=ExpenseSchema)
def detail_expense(request, pk: int):
    return get_object_or_404(Expense, pk=pk)


@router.post('expenses', response={HTTPStatus.CREATED: ExpenseSchema})
def create_expense(request, payload: ExpenseCreateSchema):
    return Expense.objects.create(**payload.dict())


@router.patch('expenses/{pk}', response=ExpenseSchema)
def update_expense(request, pk: int, payload: ExpenseCreateSchema):
    instance = get_object_or_404(Expense, pk=pk)
    data = payload.dict()

    for attr, value in data.items():
        setattr(instance, attr, value)

    instance.save()
    return instance


@router.delete('expenses/{pk}')
def delete_expense(request, pk: int):
    instance = get_object_or_404(Expense, pk=pk)
    instance.delete()
    return {'success': True}
```

backend/core/templates/base.html
    Mostrar os links Pico.css, AlpineJS e Axios
    Mostrar block js

```html
{% block js %}{% endblock js %}
```

Mostrar backend/core/templates/core/index.html



Mostrar backend/expense/templates/expense/expense.html

```html

```