from django import forms
from django.forms import ModelForm
from .models import Seller


class SellerForm(ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'
        exclude = ['user']
        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'phone': '',
            'profile_pic': '',
        }
