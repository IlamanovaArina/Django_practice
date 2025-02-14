from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django import forms
from users.models import CustomUser


class MyUserCreation(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['email', 'avatar', 'phone_number', 'country', 'username',]
        # fields = '__all__'

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен содержать только цифры.')
        return phone_number

    def __init__(self, *args, **kwargs):
        super(MyUserCreation, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите электронную почту'
        })
        self.fields['avatar'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Добавьте изображение'
        })
        self.fields['phone_number'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите номер телефона'
        })
        self.fields['country'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите страну проживания'
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите имя пользователя'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите тот же пароль'
        })


class CustomAuthenticationForm(AuthenticationForm):
    model = CustomUser
    fields = ['email', ]

    # def __init__(self, *args, **kwargs):
    #     super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
    #     self.fields['email'].widget.attrs.update({
    #         'class': 'form-control',
    #         'placeholder': 'Введите электронную почту'
    #     })
    #     self.fields['password'].widget.attrs.update({
    #         'class': 'form-control',
    #         'placeholder': 'Введите электронную почту'
    #     })

class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите электронную почту'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите электронную почту'
        })