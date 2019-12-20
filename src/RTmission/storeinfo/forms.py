from django import forms
from django.core import validators

from .models import UserInfo

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = [
            'name',
            'email',
            'phone',
            'age',
            'gender',
            'comment'
        ]
    
    CHOICES = [
        ('MALE' , 'Male'),
        ('FEMALE' , 'Female')
    ]

    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, required=False)

    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age < 1 or age > 200:
            raise forms.ValidationError("enter a valid age from 1 to 200")
        return age

