from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import login, logout,authenticate
from django.views.generic import CreateView
from .forms import customersigninform,restaurantsigninform
from django.contrib.auth.forms import AuthenticationForm
from .models import User,Customer,Restaurant

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import RestaurantSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from django.urls import reverse
import geocoder
from slots.models import Table

from notifications.models import Notification

import stripe
stripe.api_key = "sk_test_51HsOHXBgvLd18Hnhc61pr54p389M6m8t9RrugGASZCQwopeEa0Cigjnb3oLyoCdEghW2wMhoODNqq5MB7IwqQxpn006W0Fk8nm"

g = geocoder.ip('me')
lat=g.lat
lng=g.lng


@csrf_exempt
@api_view(['GET'])
def restaurant_view(request):

    if request.method == 'GET' :
        events = Restaurant.objects.all()
        serializer = RestaurantSerializer(events,many=True)
        return JsonResponse(serializer.data , safe=False)
    return JsonResponse(serializer.errors,status=400)

def resthome(request):
    context = {
            'count': Notification.objects.filter(dest_user=request.user, viewed=False, type="App")|
                             Notification.objects.filter(dest_user=request.user, viewed=False, type="General")|
                             Notification.objects.filter(dest_user=request.user, viewed=False, type="order")|
                             Notification.objects.filter(dest_user=request.user, viewed=False, type="Payment"),

            'count_a': Notification.objects.filter(dest_user=request.user, viewed=False, type="App"),
            'count_g': Notification.objects.filter(dest_user=request.user, viewed=False, type="General"),
            'count_o': Notification.objects.filter(dest_user=request.user, viewed=False, type="Order"),
            'count_p': Notification.objects.filter(dest_user=request.user, viewed=False, type="Payment"),
            }
    return render(request,'restaurant/resthomepage.html',context)

def mainhome(request):
    g = geocoder.ip('me')
    lat=g.lat
    lng=g.lng
    if request.method=='GET':
       if request.GET.get('submit')=='mylocation':
           lat=float(request.GET.get('lat'))
           lng=float(request.GET.get('lon'))
           print("lat long ",lat,lng)
    temp = []
    locations=[]
    temp.append(lat)
    temp.append(lng)
    locations.append(temp)
    data=Restaurant.objects.all()
    address = [ '#']
    for val in data:
        temp=[]
        temp.append(val.lat)
        temp.append(val.lon)
        locations.append(temp)
        address.append("profiles/"+val.user.username)
    print("Locations ",locations)
    context = {
        'locations' : locations,
        'address':address,
        'lat':lat,
        'log':lng,

        'count': Notification.objects.filter(dest_user=request.user, viewed=False, type="App")|
                         Notification.objects.filter(dest_user=request.user, viewed=False, type="General")|
                         Notification.objects.filter(dest_user=request.user, viewed=False, type="order")|
                         Notification.objects.filter(dest_user=request.user, viewed=False, type="Payment"),

        'count_a': Notification.objects.filter(dest_user=request.user, viewed=False, type="App"),
        'count_g': Notification.objects.filter(dest_user=request.user, viewed=False, type="General"),
        'count_o': Notification.objects.filter(dest_user=request.user, viewed=False, type="Order"),
        'count_p': Notification.objects.filter(dest_user=request.user, viewed=False, type="Payment"),

    }
    return render(request,'restaurant/homepage.html',context)


def main(request):
    return render(request,'restaurant/main.html')

def Signup(request):
   return render(request,'restaurant/register.html')

# Create your views here.
class customer_register(CreateView):
    model = User
    form_class = customersigninform
    template_name = 'restaurant/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

class restaurant_register(CreateView):
    model = User
    form_class = restaurantsigninform
    template_name = 'restaurant/restaurant_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                if user.is_restaurant:
                   return redirect('rest')
                else:
                    return redirect('cust')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'restaurant/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('main')


def tables(request):
    if request.method=="POST":
        tables_2 = request.POST.get('tables_2')
        tables_4 = request.POST.get('tables_4')
        tables_6 = request.POST.get('tables_6')
        tables_8 = request.POST.get('tables_8')
        x = User.objects.get(username=request.user.username)
        num_results = Table.objects.filter(user_name_id = x.id).count()
        if num_results == 0:
            z = Table(user_name=x,tables_2=tables_2,tables_4=tables_4,tables_6=tables_6,tables_8=tables_8)
            z.save()
            return redirect('rest')
        else:
            y = Table.objects.get(user_name=x)
            y.tables_2 = tables_2
            y.tables_4 = tables_4
            y.tables_6 = tables_6
            y.tables_8 = tables_8
            y.save()
            return redirect('rest')
    else:
        render(request,'restaurant/resthomepage.html',context)


def index2(request):
    return render(request,'restaurant/template2.html')

def charge2(request):
    if request.method == 'POST':
        print('Data:', request.POST)

        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['nickname'],
            source=request.POST['stripeToken'],
            address={
               'line1': '510 Townsend St',
               'postal_code': '98140',
               'city': 'San Francisco',
               'state': 'CA',
               'country': 'US',
             },

            )

        charge = stripe.Charge.create(
            customer=customer,
            amount = amount*100,
            currency='usd',
            description="payment",
        )

    return redirect(reverse('success2', args=[amount]))

def successMsg2(request, args):
    amount = args
    return render(request,'restaurant/success2.html',{'amount':amount})


def index(request):
    return render(request,'restaurant/index.html')

def charge(request):
    amount = 5
    if request.method == 'POST':
        print('Data:', request.POST)

        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['nickname'],
            source=request.POST['stripeToken'],
            address=
            {
               'line1': '510 Townsend St',
               'postal_code': '98140',
               'city': 'San Francisco',
               'state': 'CA',
               'country': 'US',
             },

            )

        charge = stripe.Charge.create(
            customer=customer,
            amount = 500,
            currency='usd',
            description="payment",
        )
    return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
    amount = args
    return render(request,'restaurant/success.html',{'amount':amount})


def index3(request,username,cost):
    context = {
    'cost':cost,
    'username':username
    }
    return render(request,'restaurant/index3.html',context)

def charge3(request,username,cost):
    amount = cost
    if request.method == 'POST':
        print('Data:', request.POST)

        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['nickname'],
            source=request.POST['stripeToken'],
            address=
            {
               'line1': '510 Townsend St',
               'postal_code': '98140',
               'city': 'San Francisco',
               'state': 'CA',
               'country': 'US',
             },

            )

        charge = stripe.Charge.create(
            customer=customer,
            amount = 500,
            currency='usd',
            description="payment",
        )
    return redirect('success3', username=username, args=amount)


def success3(request, username, args):
    amount = args
    return render(request,'restaurant/success3.html',{'amount':amount,'username':username})
