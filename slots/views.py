from django.shortcuts import render,redirect
# Create your views here.
from .models import Slot


def slot(request):
    if request.method=="POST":

        date = request.POST.get('slot_date')
        context = {
                'slot' : Slot.objects.filter(date=date)
                   }
        return redirect('/slot')
    else:
        context = {
                'slot' : Slot.objects.all()
        }
        return render(request,'slots/view_slot.html',context)


def book_slot(request):
    if request.method=="POST":
        user_name = request.POST.get('user_name')
        rest_name = request.POST.get('rest_name')
        slot_number = request.POST.get('slot_number')
        date = request.POST.get('slot_date')
        table_no = request.POST.get('table_no')

        x = Slot(user_name=user_name,rest_name=rest_name,slot_number=slot_number,date=date,table_no=table_no)
        x.save()
        return redirect('/slot')
    else:
        return render(request,'slots/book_slot.html')
