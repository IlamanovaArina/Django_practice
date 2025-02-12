from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from catalog import forms
from users.models import CustomUser


class MyUserCreation(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['email', 'password']
        # fields = '__all__'

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен содержать только цифры.')
        return phone_number

    class CustomAuthenticationForm(AuthenticationForm):
        pass