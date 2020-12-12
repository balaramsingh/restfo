from django import forms
from django.db import models

from .models import Notification

class AcceptanceForm(forms.Form):
    Choices = (('A', 'Accept'), ('R', 'Reject'))
    choice = forms.ChoiceField(choices=Choices, widget=forms.RadioSelect)

class PaymentForm(forms.Form):
    Choices = (('A', 'Received'), ('R', 'Not-Recieved'))
    choice = forms.ChoiceField(choices=Choices, widget=forms.RadioSelect)

class ReplyForm(forms.Form):
    reply = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":40}))
    class Meta:
        model = Notification
        fields = ['reply']
