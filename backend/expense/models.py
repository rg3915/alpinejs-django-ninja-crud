from datetime import datetime

from django.db import models


class Expense(models.Model):
    description = models.CharField('descrição', max_length=120)
    value = models.DecimalField('valor', max_digits=7, decimal_places=2)
    date_payment = models.DateField('data', null=True, blank=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'despesa'
        verbose_name_plural = 'despesas'

    def __str__(self):
        return f'{self.description}'

    def date_payment_display(self):
        if self.date_payment:
            date_str = self.date_payment.isoformat()
            iso_date = datetime.fromisoformat(date_str)
            return iso_date.strftime('%d/%m/%Y')
