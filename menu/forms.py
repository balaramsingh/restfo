from django.forms import ModelForm

from .models import Menu

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = ['fname','price','category','veg','availability','quantity','Image']