from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Notification
from django.contrib.auth.decorators import login_required

from restaurant.models import User
from .forms import AcceptanceForm, PaymentForm, ReplyForm

@login_required
def notifications(request):
    return render(request, 'notifications/base.html')

def show_app(request, notification_id):
    context = {
        'notification': Notification.objects.get(id=notification_id),
    }
    return render(request, 'notifications/app_notifications.html', context)


def show_gen(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    context = {
        'notification': Notification.objects.get(id=notification_id),
        'form': ReplyForm()
    }
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            a = User.objects.get(username=notification.curr_user)
            b = a.notification_set.create(title=notification.title, message=form.cleaned_data['reply'],curr_user=notification.dest_user,type="General")
        return redirect('/notifications')

    return render(request, 'notifications/gen_notifications.html', context)


def show_ord(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    user = User.objects.get(username=request.user.username)

    context = {
        'notification': Notification.objects.get(id=notification_id),
        'user': user,
        'form': AcceptanceForm()
    }
    if request.method == 'POST':
        form = AcceptanceForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['choice'] == 'A':
                a = User.objects.get(username=notification.curr_user)
                b = a.notification_set.create(title="Order Recieved", message="Your Order has been received successfully.!!..Proceed Further With Payment.!!..Thanks!",
                curr_user=notification.dest_user,type="Order")
            elif form.cleaned_data['choice'] == 'R':
                a = User.objects.get(username=notification.curr_user)
                b = a.notification_set.create(title="Order Cancelled", message="Sorry!!..Your Order has been cancelled because of unavailability of item.!!..Money Paid will be refunded.!!",
                curr_user=notification.dest_user,type="Order")
        return redirect('/notifications')

    return render(request, 'notifications/ord_notifications.html', context)


def show_pay(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    user = User.objects.get(username=request.user.username)

    context = {
        'notification': Notification.objects.get(id=notification_id),
        'user': user,
        'form': PaymentForm()
    }
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['choice'] == 'A':
                a = User.objects.get(username=notification.curr_user)
                b = a.notification_set.create(title="Payment Done", message="Your Payment has been received successfully.!!..Thanks.!!..Enjoy Food.!!",
                curr_user=notification.dest_user,type="Payment")
            elif form.cleaned_data['choice'] == 'R':
                a = User.objects.get(username=notification.curr_user)
                b = a.notification_set.create(title="Payment Not Recieved", message="Sorry.!!..Your Payment was not received.!!..Please Check Once.!!",
                curr_user=notification.dest_user,type="Payment")
        return redirect('/notifications')

    return render(request, 'notifications/pay_notifications.html', context)


def delete_notification(request, notification_id):
    n = Notification.objects.get(id=notification_id)
    n.viewed = True
    n.save()
    return redirect('/notifications')


def give_g(request,usrname):
    a = User.objects.get(username=usrname)
    b = a.notification_set.create(title=request.POST['title'], message=request.POST['message'], curr_user=request.user.username,type="General")
    b.save()
    return redirect('/notifications')

def give_o(request,usrname):
    a = User.objects.get(username=usrname)
    b = a.notification_set.create(order=request.POST['order'], message=request.POST['message'], curr_user=request.user.username,type="Order")
    b.save()
    return redirect('/notifications')

def give_p(request,usrname):
    a = User.objects.get(username=usrname)
    b = a.notification_set.create(title=request.POST['title'], message=request.POST['message'], curr_user=request.user.username,type="Payment")
    b.save()
    return redirect('/notifications')


def give_g_notification(request,usrname):
    context = {
       'users' : User.objects.all()
    }
    return render(request, 'notifications/give_gen.html', context)


def give_o_notification(request,usrname):
    context = {
       'users' : User.objects.all()
    }
    return render(request, 'notifications/give_order.html', context)

def give_p_notification(request,usrname):
    context = {
       'users' : User.objects.all()
    }
    return render(request, 'notifications/give_payment.html', context)


@login_required
def loggedin_a(request):
    context = {
        'full_name': request.user.username,
        'notifications': Notification.objects.filter(dest_user=request.user, viewed=False, type="App"),
    }
    return render(request, 'notifications/view_app.html', context)

@login_required
def loggedin_g(request):
    context = {
        'full_name': request.user.username,
        'notifications': Notification.objects.filter(dest_user=request.user, viewed=False, type="General"),
    }
    return render(request, 'notifications/view_general.html', context)

@login_required
def loggedin_o(request):
    context = {
        'full_name': request.user.username,
        'notifications': Notification.objects.filter(dest_user=request.user, viewed=False, type="Order"),
    }
    return render(request, 'notifications/view_order.html', context)

@login_required
def loggedin_p(request):
    context = {
        'full_name': request.user.username,
        'notifications': Notification.objects.filter(dest_user=request.user, viewed=False, type="Payment"),
    }
    return render(request, 'notifications/view_pay.html', context)
