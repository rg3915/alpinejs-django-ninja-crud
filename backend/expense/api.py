
from ninja import Router
from ninja.orm import create_schema

from .models import Expense

router = Router(tags=['Expenses'])


ExpenseSchema = create_schema(Expense)
