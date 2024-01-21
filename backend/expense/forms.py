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
