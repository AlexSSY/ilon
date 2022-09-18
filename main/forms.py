import re
from django import forms
from django.core.exceptions import ValidationError
from .models import Person

class MainForm(forms.ModelForm):
    template_name = 'main/form_snippet.html'
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'email', 'phone', 'password')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'first_name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'last_name'}),
            'email': forms.TextInput(attrs={'placeholder': 'email'}),
            'phone': forms.TextInput(attrs={'placeholder': '+39 434 34 56', 'type': 'tel'}),
            'password': forms.TextInput(attrs={'placeholder': 'password'}),
        }

        def clean_phone(self):
            phone = self.cleaned_data['phone']
            if not re.fullmatch(r'\+[0-9]{8,13}', phone):
                raise ValidationError('Phone number incorrect')
            return phone