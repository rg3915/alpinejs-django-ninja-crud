from django.contrib import admin

from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'value', 'date_payment')
    readonly_fields = ('created',)
    search_fields = ('description',)
    date_hierarchy = 'created'
