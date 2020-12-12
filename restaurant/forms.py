from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Customer, User,Restaurant

class customersigninform(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    contact = forms.CharField(required=True)
    gmail = forms.CharField(required=True)
  
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.phone_number=self.cleaned_data.get('phone_number')
        customer.gmail=self.cleaned_data.get('gmail')
        customer.save()
        return user


class restaurantsigninform(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    Restaurant_Name=forms.CharField(required=True)
    gmail = forms.CharField(required=True)
    Address=forms.CharField(required=True)
    Restaurant_Type=forms.CharField(required=True)
    Restaurant_Image=forms.ImageField(required=True)
    Food_Type=forms.CharField(required=True)
    contact = forms.CharField(required=True)
    Payment_No = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User


    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_restaurant = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        restaurant = Restaurant.objects.create(user=user)
        restaurant.Restaurant_Name=self.cleaned_data.get('Restaurant_Name')
        restaurant.gmail=self.cleaned_data.get('Gmail')
        restaurant.Address=self.cleaned_data.get('Address')
        restaurant.Restaurant_Type=self.cleaned_data.get('Restaurant_Type')
        restaurant.Food_Type=self.cleaned_data.get('Food_Type')
        restaurant.Restaurant_Image=self.cleaned_data.get('Restaurant_Image')
        restaurant.contact=self.cleaned_data.get('contact')
        restaurant.Payment_No=self.cleaned_data.get('Payment_No')
        restaurant.save()
        return user



