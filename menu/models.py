from django.db import models
from restaurant.models import Restaurant,Customer
from PIL import Image

class Menu(models.Model):
    food_type = [('Starters','Starters'),('Main Course','Main Course'),
    ('Indian Breads','Indian Breads'),('Snacks','Snacks'),('Deserts','Deserts'),('Ice Creams','Ice Creams')]
    status=[('unav','Unavailable'),('av','Available')]
    id 		 = models.AutoField(primary_key=True)
    fname 		= models.CharField(max_length=30,blank=False,default='val None')
    r_id     = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    price    = models.IntegerField(blank=False)
    category 	= models.CharField(max_length=50,blank=False,choices=food_type,default='val None')
    veg         = models.BooleanField(default=True)
    availability = models.CharField(max_length=15,default='Unavailable',choices=status)
    quantity = models.IntegerField(blank=False,default=0)
    Image = models.ImageField(default='/menuimg/default.jpg', upload_to='media')
    rating =  models.IntegerField(blank=False,default=0)
    no_of_rated = models.IntegerField(blank=False,default=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        super(Menu, self).save()
        img = Image.open(self.Image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.Image.path)
    


class Order(models.Model):
    Orderid    =  models.AutoField(primary_key=True)
    OrderedBy  =  models.ForeignKey(Customer,on_delete=models.CASCADE)
    Menu_id    =  models.ForeignKey(Menu,on_delete=models.CASCADE)
    Timestamp  =  models.DateTimeField(auto_now_add=True)
    R_id	   =  models.ForeignKey(Restaurant ,on_delete=models.CASCADE)
    quantity   =  models.IntegerField(default=0)
    cost       =  models.IntegerField(default=0)
    ORDER_STATE_CHOICES = (
		('ORDER_STATE_PENDING','ORDER_STATE_PENDING'),
	    ('ORDER_STATE_CONFIRMED','ORDER_STATE_CONFIRMED'),
        ('ORDER_STATE_CANNOT_BE_PROCESSED','ORDER_STATE_CANNOT_BE_PROCESSED'),
	    ('ORDER_STATE_COMPLETED', 'ORDER_STATE_COMPLETED'),
    )
    Status = models.CharField(max_length=50,choices=ORDER_STATE_CHOICES,default='ORDER_STATE_PENDING')

    def __str__(self):
        return str(self.Orderid) +' '+self.Status


    
