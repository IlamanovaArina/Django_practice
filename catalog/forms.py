from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product

SPAMS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар', ]

class EditingForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'description', 'imagery', 'price', 'category']
        exclude = ['created_at', 'updated_at', ]

    def __init__(self, *args, **kwargs):
        super(EditingForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-check',
            'placeholder': 'Введите название'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-check ',
            'placeholder': 'Введите описание'
        })
        self.fields['imagery'].widget.attrs.update({
            'class': 'form-check',
            'placeholder': 'Добавьте изображение'
        })
        self.fields['price'].widget.attrs.update({
            'class': 'form-check',
            'placeholder': '10 000'
        })
        self.fields['category'].widget.attrs.update({
            'class': 'form-check',
            'placeholder': 'Выберите категорию'
        })

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name').lower()
        description = cleaned_data.get('description').lower()
        for spam in SPAMS:
            if spam in name:
                self.add_error('name', f'Имя не может содержать запрещённые слова. Вы ввели: {spam}')
            if spam in description:
                self.add_error('description', f'Описание не может содержать запрещённые слова. Вы ввели: {spam}')


    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не должна быть отрицательной')
