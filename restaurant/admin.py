from django.contrib import admin

# Register your models here.

from restaurant.models import User,Customer,Restaurant

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Restaurant)
