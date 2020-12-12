from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from restaurant.models import Restaurant,User
from slots.models import Slot,Table

from rest_framework.decorators import api_view
from .models import Api1,Api2,Review
from rest_framework.parsers import JSONParser
from .serializers import Api1Serializer,Api2Serializer,ReviewSerializer
# Create your views here.

from django.utils.dateparse import parse_date
from django.views.decorators.csrf import csrf_exempt

from .models import Review

def profile_view(request,username):
    x = User.objects.get(username=username)
    rest = Restaurant.objects.get(user_id=x.id)
    context = {
        'rest':rest,
        'username':username
        }
    if request.method=="POST":
        user_name = request.user.username
        rest_name = username
        slot_number = request.POST.get('slot_number')
        date = request.POST.get('slot_date')
        table_no = request.POST.get('table_no')

        check = availability(rest_name,slot_number,date,table_no)
        if check :
            x = Slot(user_name=user_name,rest_name=rest_name,slot_number=slot_number,date=date,table_no=table_no)
            print("Success")
            context['message'] = 'Booking Successful'
            x.save()
        else :
            context['message'] = 'No tables available'
            print("ERRORRR")
        return render(request,"profiles/profile_view.html",context)
    else:
        return render(request,"profiles/profile_view.html",context)

def availability(restaurantname,slot_number,date,table_no):
    k = Slot.objects.filter(rest_name = restaurantname,date=date,slot_number=slot_number,table_no=table_no).count()
    x = User.objects.get(username=restaurantname)
    y = Table.objects.get(user_name=x)
    if int(table_no) == 2 :
        if y.tables_2 > k :
            return True
        return False
    elif int(table_no) == 4 :
        if y.tables_4 > k :
            return True
        return False
    elif int(table_no) == 6 :
        if y.tables_6 > k :
            return True
        return False
    elif int(table_no) == 8 :
        if y.tables_8 > k :
            return True
        return False
    else :
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        return False


def check_view(request,username):
    context = {
        'username':username,
        'available_2' : ['0'],
        'available_4' : ['0'],
        'available_6' : ['0'],
        'available_8' : ['0'],
        'occupied_2' : ['0'],
        'occupied_4' : ['0'],
        'occupied_6' : ['0'],
        'occupied_8' : ['0'],
    }
    if request.method == 'POST' :
        rest_name = username
        slot_number = request.POST.get('slot_number')
        date = request.POST.get('slot_date')

        x = User.objects.get(username=username)
        y = Table.objects.get(user_name=x)

        occupied_2 = Slot.objects.filter(rest_name = username,date=date,slot_number=slot_number,table_no='2').count()
        occupied_4 = Slot.objects.filter(rest_name = username,date=date,slot_number=slot_number,table_no='4').count()
        occupied_6 = Slot.objects.filter(rest_name = username,date=date,slot_number=slot_number,table_no='6').count()
        occupied_8 = Slot.objects.filter(rest_name = username,date=date,slot_number=slot_number,table_no='8').count()

        t_2 = y.tables_2
        t_4 = y.tables_4
        t_6 = y.tables_6
        t_8 = y.tables_8

        a_2 = t_2 - occupied_2
        a_4 = t_4 - occupied_4
        a_6 = t_6 - occupied_6
        a_8 = t_8 - occupied_8

        two = []
        for i in range(a_2):
            two.append(i)
        four = []
        for i in range(a_4):
           four.append(i)
        six = []
        for i in range(a_6):
            six.append(i)
        eight = []
        for i in range(a_8):
            eight.append(i)

        two_o = []
        for i in range(occupied_2):
            two_o.append(i)
        four_o = []
        for i in range(occupied_4):
            four_o.append(i)
        six_o = []
        for i in range(occupied_6):
            six_o.append(i)
        eight_o = []
        for i in range(occupied_8):
            eight_o.append(i)

        context = {
        'available_2' : two,
        'available_4' : four,
        'available_8' : eight,
        'available_6' : six,
        'occupied_2' : two_o,
        'occupied_4' : four_o,
        'occupied_6' : six_o,
        'occupied_8' : eight_o,
    }

        return render(request,'profiles/check_view.html',context)
    else :

        return render(request,'profiles/check_view.html',context)


def check_view2(request,username):
    context = {
        'username':username,
    }
    for i in range(1,21):
        str1 = 'slot_' + str(i)
        context[str1] = '1'
    if request.method == 'POST' :
        rest_name = username
        table_no = request.POST.get('table_no')
        date = request.POST.get('slot_date')

        ans = Slot.objects.filter(rest_name=username,table_no=table_no)
        modify = []

        for obj in ans :
            a = Slot(obj)
            k = int(obj.slot_number)
            check = availability(username,k,date,table_no)
            if check == False :
                modify.append(int(k))

        print(modify)
        for k in modify:
            str1 = 'slot_' + str(k)
            context[str1] = '0'

        return render(request,'profiles/check_view2.html',context)
    else :
        return render(request,'profiles/check_view2.html',context)


def time_slot(request):
    return render(request, 'profiles/time_slots.html')

class api1response :
    def __init__(self, a_2,a_4,a_6,a_8):
        self.available_2 = a_2
        self.available_4 = a_4
        self.available_6 = a_6
        self.available_8 = a_8


@csrf_exempt
@api_view(['GET'])
def api_view1(request,username,date_api,slot_no):
    if request.method == 'GET' :
        rest_name = username
        slot_number = slot_no
        date = parse_date(date_api)

        x = User.objects.get(username=username)
        y = Table.objects.get(user_name=x)

        occupied_2 = Slot.objects.filter(rest_name = username,date=date,slot_number=slot_number,table_no='2').count()
        occupied_4 = Slot.objects.filter(rest_name = username,date=date,slot_number=slot_number,table_no='4').count()
        occupied_6 = Slot.objects.filter(rest_name = username,date=date,slot_number=slot_number,table_no='6').count()
        occupied_8 = Slot.objects.filter(rest_name = username,date=date,slot_number=slot_number,table_no='8').count()

        t_2 = y.tables_2
        t_4 = y.tables_4
        t_6 = y.tables_6
        t_8 = y.tables_8

        a_2 = t_2 - occupied_2
        a_4 = t_4 - occupied_4
        a_6 = t_6 - occupied_6
        a_8 = t_8 - occupied_8

        obj = Api1(restaurant_name=username,date=date,slot_number=slot_no,available_2_seater_tables=a_2,available_4_seater_tables=a_4,available_6_seater_tables=a_6,available_8_seater_tables=a_8)

        serializer = Api1Serializer(obj)
        return JsonResponse(serializer.data , safe=False)


@csrf_exempt
@api_view(['GET'])
def api_view2(request,username,date_api,table_size):
    if request.method == 'GET' :
        table_no = table_size
        date = parse_date(date_api)
        context = {
        'username':username,
        }
        for i in range(1,21):
            str1 = 'slot_' + str(i)
            context[str1] = '1'
        ans = Slot.objects.filter(rest_name=username,table_no=table_no)
        modify = []
        for obj in ans :
            a = Slot(obj)
            k = int(obj.slot_number)
            check = availability(username,k,date,table_no)
            if check == False :
                modify.append(int(k))
        for k in modify:
            str1 = 'slot_' + str(k)
            context[str1] = '0'
        mod = {
            '1' : 'available' ,
            '0' : 'not available'
        }
        obj = Api2(restaurant_name=username,date=date,table_size=table_no,slot_1_status=mod[context['slot_1']],slot_2_status=mod[context['slot_2']],slot_3_status=mod[context['slot_3']],slot_4_status=mod[context['slot_4']],slot_5_status=mod[context['slot_5']],
                slot_6_status=mod[context['slot_6']],slot_7_status=mod[context['slot_7']],slot_8_status=mod[context['slot_8']],slot_9_status=mod[context['slot_9']],slot_10_status=mod[context['slot_10']],
                slot_11_status=mod[context['slot_11']],slot_12_status=mod[context['slot_12']],slot_13_status=mod[context['slot_13']],slot_14_status=mod[context['slot_14']],slot_15_status=mod[context['slot_15']],
                slot_16_status=mod[context['slot_16']],slot_17_status=mod[context['slot_17']],slot_18_status=mod[context['slot_18']],slot_19_status=mod[context['slot_19']],slot_20_status=mod[context['slot_20']])

        serializer = Api2Serializer(obj)
        return JsonResponse(serializer.data , safe=False)

def give_review(request,username):
    x = User.objects.get(username=username)
    if request.method=="POST":
        rest_name = request.POST.get('restaurantName')
        review = request.POST.get('restaurantreview')
        experience = request.POST.get('exp')
        rating = request.POST.get('rating')
        a = x.review_set.create(rest_name=rest_name,review=review,experience=experience,rating=rating)
        a.save()
        return redirect('show',username)
    else:
        return render(request,'profiles/reviewrating.html')

def show(request,username):
    x = User.objects.get(username=username)
    reviews = Review.objects.filter(rest_user=x.id)
    context = {
    'reviews':reviews,
    }
    return render(request,'profiles/show.html',context)

@api_view(['GET'])
def ReviewAPI(request,username):
    if request.method == 'GET' :
        x = User.objects.get(username=username)
        reviews = Review.objects.filter(rest_user=x.id)
        serializer = ReviewSerializer(reviews,many = True)
        return JsonResponse(serializer.data,safe=False)
    return JsonResponse(serializer.errors,status=400)

