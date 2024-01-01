from http import HTTPStatus

from django.shortcuts import get_object_or_404
from ninja import ModelSchema, Router
from ninja.orm import create_schema

from .models import Expense

router = Router(tags=['Expenses'])


ExpenseSchema = create_schema(Expense)
