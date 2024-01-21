from http import HTTPStatus

from django.shortcuts import get_object_or_404
from ninja import ModelSchema, Router
from ninja.orm import create_schema

from .models import Expense

router = Router(tags=['Expenses'])


ExpenseSchema = create_schema(
    Expense, custom_fields=(('date_payment_display', str, None),)
)


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
