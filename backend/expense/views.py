from django.shortcuts import render

from .forms import ExpenseForm


def expense_list(request):
    template_name = 'expense/expense.html'
    form = ExpenseForm
    context = {'form': form}
    return render(request, template_name, context)
