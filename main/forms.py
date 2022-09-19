import re
from django import forms
from django.core.exceptions import ValidationError
from .models import Person
from django.utils.translation import gettext as _

class MainForm(forms.ModelForm):
    template_name = 'main/form_snippet.html'
    class Meta:
        model = Person

        fields = ('first_name', 'last_name', 'email', 'phone', 'password')

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': _('Имя')}),
            'last_name': forms.TextInput(attrs={'placeholder': _('Фамилия')}),
            'email': forms.EmailInput(attrs={'placeholder': _('Почта')}),
            'phone': forms.TextInput(attrs={'placeholder': _('+39 434 34 56'), 'type': 'tel'}),
            'password': forms.PasswordInput(attrs={'placeholder': _('Пароль')}),
        }
        
        error_messages = {
            'email': {
                'invalid' : _('Введите корректный email (example@mail.com)'),
            },
        }

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not re.fullmatch(r'\+[0-9]{8,13}', phone):
            raise ValidationError(_('Некорректный номер телефона'), code='invalid')
        return phone

    def clean_password(self):
        password = self.cleaned_data['password']
        if not re.fullmatch(r'^(?=.*[A-Za-z])[A-Za-z\d]{8,}$', password):
            raise ValidationError(_('Пароль должен содержать минимум 8 символов и одну букву'))
        return password