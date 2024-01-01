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

mkdir -p backend/core/templates/core
touch backend/core/templates/base.html
touch backend/core/templates/core/index.html

mkdir -p backend/expense/templates/expense
touch backend/expense/templates/expense/expense.html
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
        super(ExpenseForm, self).__init__(*args, **kwargs)

        self.fields['value'].widget.attrs['min'] = 0
```


```python
# backend/expense/api.py
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


Mostrar backend/core/templates/core/index.html



Mostrar backend/expense/templates/expense/expense.html
