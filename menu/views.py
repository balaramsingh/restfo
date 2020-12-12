from django.shortcuts import render,HttpResponse,redirect
from .forms import MenuForm
from restaurant.models import User,Restaurant as RestUser,Customer as CustUser
from .models import Menu, Order
from restaurant.models import User
from django.utils.timezone import timezone
# Create your views here.
from django.contrib.auth.decorators import login_required
from rest_framework.decorators  import api_view
from rest_framework.response import Response
from .serializers import MenuSerialiser
from django.http import HttpResponse, JsonResponse
def menu_items(restid):
    Starters =  Menu.objects.filter(r_id__user__username = restid,  category="Starters")
    Main_Course  =  Menu.objects.filter(r_id__user__username = restid, category='Main Course')
    Indian_Breads = Menu.objects.filter(r_id__user__username = restid, category='Indian Breads')
    Snacks  =  Menu.objects.filter(r_id__user__username = restid, category='Snacks')
    Deserts =  Menu.objects.filter(r_id__user__username = restid, category='Deserts')
    Ice_Creams = Menu.objects.filter(r_id__user__username = restid, category='Ice Creams')
    return Starters,Main_Course,Indian_Breads,Snacks,Deserts,Ice_Creams

@login_required
def update(request,menuid):
    item = Menu.objects.get(id=menuid)

    if request.method == 'POST':
        form = MenuForm(request.POST,request.FILES)
        print(request.POST.get('status'))
        if form.is_valid():
            instance = Menu.objects.get(id=menuid)
            instance.fname = form.cleaned_data.get('fname')
            instance.price = form.cleaned_data.get('price')
            instance.category = form.cleaned_data.get('category')
            instance.availability  = form.cleaned_data.get('availability')
            instance.quantity = form.cleaned_data.get('quantity')
            instance.Image = form.cleaned_data.get('Image')
            instance.save()
            return redirect('menu_view')
    else:
        form = MenuForm()
    return render(request,'menu/menu_update.html',context={'form':form,'item':item})

@login_required
def menuview(request):
    restid =request.user
    menu = Menu.objects.filter(r_id__user__username = request.user)
    Starters,Main_Course,Indian_Breads,Snacks,Deserts,Ice_Creams = menu_items(request.user)
    rest_user=RestUser.objects.get(user__username=request.user)
    if request.method == 'POST':
        form = MenuForm(request.POST,request.FILES)
        if form.is_valid():
            if request.POST.get('submit')=='Update':
               print("update")
            else:
                instance=Menu()
                rest_user = User.objects.get(username=request.user)
                instance.fname = form.cleaned_data.get('fname')
                instance.price = form.cleaned_data.get('price')
                instance.category = form.cleaned_data.get('category')
                instance.availability  = form.cleaned_data.get('availability')
                instance.quantity = form.cleaned_data.get('quantity')
                instance.r_id = RestUser.objects.get(user=rest_user)
                # instance.Image =form.cleaned_data.get('Image')
                instance.Image = form.cleaned_data.get('Image')
                #print(form.cleaned_data.get('Image'))
                instance.save()
                return redirect('menu_view')
        if request.POST.get('submit')=='Delete':
            id=request.POST.get('menuid')
            try:
                instance = Menu.objects.get(id=id)
                instance.delete()
            except Menu.DoesNotExist:
                instance=None
    else:
        form = MenuForm()
    if request.GET.get('submit')=='Starters '+'('+str(len(Starters))+')':
            Starters,Main_Course,Indian_Breads,Snacks,Deserts,Ice_Creams = menu_items(restid)
            context={'form':form,'menu':Starters,'rest_user':rest_user,'Starters':Starters,
            'Main_Course':Main_Course,
            'Indian_Breads':Indian_Breads,'Snacks':Snacks,
            'Deserts':Deserts,'Ice_Creams':Ice_Creams,'Selected':'Starters'}
            return render(request,'menu/menu.html',context=context)

    if request.GET.get('submit')=='Main Course '+'('+str(len(Main_Course))+')':
            Starters,Main_Course,Indian_Breads,Snacks,Deserts,Ice_Creams = menu_items(restid)
            context={'form':form,'menu':Main_Course,'rest_user':rest_user,'Starters':Starters,
            'Main_Course':Main_Course,
            'Indian_Breads':Indian_Breads,'Snacks':Snacks,
            'Deserts':Deserts,'Ice_Creams':Ice_Creams,'Selected':'Main Course'}
            return render(request,'menu/menu.html',context=context)

    if request.GET.get('submit')=='Indian Breads '+'('+str(len(Indian_Breads))+')':
            Starters,Main_Course,Indian_Breads,Snacks,Deserts,Ice_Creams = menu_items(restid)
            context={'form':form,'menu':Indian_Breads,'rest_user':rest_user,'Starters':Starters,
            'Main_Course':Main_Course,
            'Indian_Breads':Indian_Breads,'Snacks':Snacks,
            'Deserts':Deserts,'Ice_Creams':Ice_Creams,'Selected':'Indian Breads'}
            return render(request,'menu/menu.html',context=context)

    if request.GET.get('submit')=='Snacks '+'('+str(len(Snacks))+')':
            Starters,Main_Course,Indian_Breads,Snacks,Deserts,Ice_Creams = menu_items(restid)
            context={'form':form,'menu':Snacks,'rest_user':rest_user,'Starters':Starters,
            'Main_Course':Main_Course,
            'Indian_Breads':Indian_Breads,'Snacks':Snacks,
            'Deserts':Deserts,'Ice_Creams':Ice_Creams,'Selected':'Snacks'}
            return render(request,'menu/menu.html',context=context)

    if request.GET.get('submit')=='Deserts '+'('+str(len(Deserts))+')':
            Starters,Main_Course,Indian_Breads,Snacks,Deserts,Ice_Creams = menu_items(restid)
            context={'form':form,'menu':Deserts,'rest_user':rest_user,'Starters':Starters,
            'Main_Course':Main_Course,
            'Indian_Breads':Indian_Breads,'Snacks':Snacks,
            'Deserts':Deserts,'Ice_Creams':Ice_Creams,'Selected':'Deserts'}
            return render(request,'menu/menu.html',context=context)

    if request.GET.get('submit')=='Ice Creams '+'('+str(len(Ice_Creams))+')':
            Starters,Main_Course,Indian_Breads,Snacks,Deserts,Ice_Creams = menu_items(restid)
            context={'form':form,'menu':Ice_Creams,'rest_user':rest_user,'Starters':Starters,
            'Main_Course':Main_Course,
            'Indian_Breads':Indian_Breads,'Snacks':Snacks,
            'Deserts':Deserts,'Ice_Creams':Ice_Creams,'Selected':'Ice Creams'}
            return render(request,'menu/menu.html',context=context)

    if request.GET.get('submit')=='Search':
            q=request.GET.get('query')
            q=Menu.objects.filter(r_id__user__username = restid,fname = q)
            context={'form':form,'menu':q,'rest_user':rest_user,'Starters':Starters,
            'Main_Course':Main_Course,
            'Indian_Breads':Indian_Breads,'Snacks':Snacks,
            'Deserts':Deserts,'Ice_Creams':Ice_Creams,'Selected':'All Items'}
            return render(request,'menu/menu.html',context=context)


    else:
        form = MenuForm()
    context={'form':form,'menu':menu,'rest_user':rest_user,'Starters':Starters,
    'Main_Course':Main_Course,
    'Indian_Breads':Indian_Breads,'Snacks':Snacks,
    'Deserts':Deserts,'Ice_Creams':Ice_Creams,'Selected':'All Items'}
    return render(request,'menu/menu.html',context=context)

@login_required
def OrderConfirm(request):
    orders=Order.objects.filter(R_id__user__username = request.user,Status='ORDER_STATE_PENDING')
    orders_confirmed=Order.objects.filter(R_id__user__username = request.user,Status='ORDER_STATE_CONFIRMED')
    if request.method == 'POST':
        if request.POST.get('submit')=='Delete Order':
            id        = request.POST.get('orderid')
            instance  = Order.objects.get(Orderid=id)
            instance.Status = 'ORDER_STATE_CANNOT_BE_PROCESSED'
            instance.save()
            orders   = Order.objects.filter(R_id__user__username = request.user,Status='ORDER_STATE_PENDING')
            return redirect('MenuOrder')

        if request.POST.get('submit')=='Confirm Order':
            id              =  request.POST.get('orderid')
            instance        =  Order.objects.get(Orderid=id)
            instance.Status = 'ORDER_STATE_CONFIRMED'
            instance.save()
            orders   = Order.objects.filter(R_id__user__username = request.user,Status='ORDER_STATE_PENDING')
            return redirect('MenuOrder')

    return render(request,"menu/orders.html",context={'user':request.user,'orders':orders,'orders_confirmed':orders_confirmed})





cart = []
cost = [0]
msg = [None]
@login_required
def User_Menu(request,restid):
    rest_user = RestUser.objects.get(user__username = restid)
    items = Menu.objects.filter(r_id__user__username = restid)
    Starters,Main_Course,Indian_Breads,Snacks,Deserts,Ice_Creams = menu_items(restid)
    if request.method=='GET':
        if request.GET.get('submit')=='My Orders':
            MyOrders = Order.objects.filter(OrderedBy__user__username = request.user)
            print(MyOrders)
            context={
            'user':request.user,'rest_user':rest_user ,
            'Menu':items,'cart':cart,'cost':cost,'msg':msg,
            'Pending':[],'Confirm':[],'MyOrders':MyOrders,'Starters':Starters,'Main_Course':Main_Course,
            'Indian_Breads':Indian_Breads,'Snacks':Snacks,
            'Deserts':Deserts,'Ice_Creams':Ice_Creams,'Selected':'All Items'}
            return render(request,'menu/user_menu.html',context=context)

        if request.GET.get('submit')=='Successful Orders':
            Successful = Order.objects.filter(OrderedBy__user__username = request.user,Status='ORDER_STATE_CONFIRMED')
            context={
            'user':request.user,'rest_user':rest_user ,
            'Menu':items,'cart':cart,'cost':cost,'msg':msg,
            'Pending':[],'Confirm':Successful,'MyOrders':[],
            'Starters':Starters,'Main_Course':Main_Course,
            'Indian_Breads':Indian_Breads,'Snacks':Snacks,
            'Deserts':Deserts,'Ice_Creams':Ice_Creams,'Selected':'All Items'}
            return render(request,'menu/user_menu.html',context=context)

        if request.GET.get('submit')=='Failed Orders':
            pending = Order.objects.filter(OrderedBy__user__username = request.user,Status='ORDER_STATE_CANNOT_BE_PROCESSED')
            context={
            'user':request.user,'rest_user':rest_user ,
            'Menu':items,'cart':cart,'cost':cost,'msg':msg,
            'Pending':pending,'Confirm':[],'MyOrders':[],
            'Starters':Starters,'Main_Course':Main_Course,
            'Indian_Breads':Indian_Breads,'Snacks':Snacks,
            'Deserts':Deserts,'Ice_Creams':Ice_Creams,'Selected':'All Items'}
            return render(request,'menu/user_menu.html',context=context)

        if request.GET.get('submit')=='Add':
            menuid    =  request.GET.get('menuid')
            Item_Name =  Menu.objects.get(id=menuid).fname
            value     =  Menu.objects.get(id=menuid).price
            quantity  =  request.GET.get('quantity')
            cost[0]   =     cost[0]+value*int(quantity)
            cart.append([Item_Name,quantity,value,menuid,cost[0]])
            print(cart)
            return redirect('UserMenu',restid=restid)

        if request.GET.get('submit')=='Confirm Your Order':
            for val in cart:
                instance = Order()
                instance.OrderedBy = CustUser.objects.get(user__username=request.user)
                instance.R_id=rest_user
                instance.Menu_id=Menu.objects.get(id=val[3])
                instance.quantity=val[1]
                instance.cost = val[-1]
                instance.save()
                msg[0]=instance.Status
                cost1 = str(instance.cost)
                cart.pop(0)
                cost[0]=cost[0]-int(val[1])*val[2]
            return redirect(str(instance.R_id.user.username)+'/index3/'+ str(cost1),instance.R_id.user.username,cost1)

        if request.GET.get('submit')=='Undo':
            if cart:
                val=cart.pop(-1)
                cost[0]=cost[0]-int(val[1])*val[2]
            return redirect('rest_list',restid=restid)
        if request.GET.get('submit')=='Starters '+'('+str(len(Starters))+')':
            print('starters')
            Starters,Main_Course,Indian_Breads,Snacks,Deserts,Ice_Creams = menu_items(restid)
            context={
            'user':request.user,'rest_user':rest_user ,
            'Menu':Starters,'cart':cart,'cost':cost,'msg':msg,
            'Pending':[],'Confirm':[],'MyOrders':[],
            'Starters':Starters,'Main_Course':Main_Course,
            'Indian_Breads':Indian_Breads,'Snacks':Snacks,
            'Deserts':Deserts,'Ice_Creams':Ice_Creams,'Selected':'Starters'}
            return render(request,'menu/user_menu.html',context=context)

        if request.GET.get('submit')=='Main Course '+'('+str(len(Main_Course))+')':
            Starters,Main_Course,Indian_Breads,Snacks,Deserts,Ice_Creams = menu_items(restid)
            context={
            'user':request.user,'rest_user':rest_user ,
            'Menu':Main_Course,'cart':cart,'cost':cost,'msg':msg,
            'Pending':[],'Confirm':[],'MyOrders':[],
            'Starters':Starters,'Main_Course':Main_Course,
            'Indian_Breads':Indian_Breads,'Snacks':Snacks,
            'Deserts':Deserts,'Ice_Creams':Ice_Creams,'Selected':'Main Course'}
            return render(request,'menu/user_menu.html',context=context)

        if request.GET.get('submit')=='Indian Breads '+'('+str(len(Indian_Breads))+')':
            Starters,Main_Course,Indian_Breads,Snacks,Deserts,Ice_Creams = menu_items(restid)
            context={
            'user':request.user,'rest_user':rest_user ,
            'Menu':Indian_Breads,'cart':cart,'cost':cost,'msg':msg,
            'Pending':[],'Confirm':[],'MyOrders':[],
            'Starters':Starters,'Main_Course':Main_Course,
            'Indian_Breads':Indian_Breads,'Snacks':Snacks,
            'Deserts':Deserts,'Ice_Creams':Ice_Creams,'Selected':'Indian Breads'}
            return render(request,'menu/user_menu.html',context=context)

        if request.GET.get('submit')=='Snacks '+'('+str(len(Snacks))+')':
            Starters,Main_Course,Indian_Breads,Snacks,Deserts,Ice_Creams = menu_items(restid)
            context={
            'user':request.user,'rest_user':rest_user ,
            'Menu':Snacks,'cart':cart,'cost':cost,'msg':msg,
            'Pending':[],'Confirm':[],'MyOrders':[],
            'Starters':Starters,'Main_Course':Main_Course,
            'Indian_Breads':Indian_Breads,'Snacks':Snacks,
            'Deserts':Deserts,'Ice_Creams':Ice_Creams,'Selected':'Snacks'}
            return render(request,'menu/user_menu.html',context=context)

        if request.GET.get('submit')=='Deserts '+'('+str(len(Deserts))+')':
            Starters,Main_Course,Indian_Breads,Snacks,Deserts,Ice_Creams = menu_items(restid)
            context={
            'user':request.user,'rest_user':rest_user ,
            'Menu':Deserts,'cart':cart,'cost':cost,'msg':msg,
            'Pending':[],'Confirm':[],'MyOrders':[],
            'Starters':Starters,'Main_Course':Main_Course,
            'Indian_Breads':Indian_Breads,'Snacks':Snacks,
            'Deserts':Deserts,'Ice_Creams':Ice_Creams,'Selected':'Deserts'}
            return render(request,'menu/user_menu.html',context=context)

        if request.GET.get('submit')=='Ice Creams '+'('+str(len(Ice_Creams))+')':
            Starters,Main_Course,Indian_Breads,Snacks,Deserts,Ice_Creams = menu_items(restid)
            context={
            'user':request.user,'rest_user':rest_user ,
            'Menu':Ice_Creams,'cart':cart,'cost':cost,'msg':msg,
            'Pending':[],'Confirm':[],'MyOrders':[],
            'Starters':Starters,'Main_Course':Main_Course,
            'Indian_Breads':Indian_Breads,'Snacks':Snacks,
            'Deserts':Deserts,'Ice_Creams':Ice_Creams,'Selected':'Ice Creams'}
            return render(request,'menu/user_menu.html',context=context)
        if request.GET.get('submit')=='Search':
            q=request.GET.get('query')
            q=Menu.objects.filter(r_id__user__username = restid,fname = q)
            context={
            'user':request.user,'rest_user':rest_user ,
            'Menu':q,'cart':cart,'cost':cost,'msg':msg,
            'Pending':[],'Confirm':[],'MyOrders':[],
            'Starters':Starters,'Main_Course':Main_Course,
            'Indian_Breads':Indian_Breads,'Snacks':Snacks,
            'Deserts':Deserts,'Ice_Creams':Ice_Creams,'Selected':'Search Results'}
            return render(request,'menu/user_menu.html',context=context)



    context={
        'user':request.user,'rest_user':rest_user ,
        'Menu':items,'cart':cart,'cost':cost,'msg':msg,
        'Pending':[],'Confirm':[],'MyOrders':[],
        'Starters':Starters,'Main_Course':Main_Course,
        'Indian_Breads':Indian_Breads,'Snacks':Snacks,
        'Deserts':Deserts,'Ice_Creams':Ice_Creams,'Selected':'All Items'}
    return render(request,'menu/user_menu.html',context=context)



@login_required
def rating(request,restid):
    menu = Menu.objects.filter(r_id__user__username = restid)
    rest_user = RestUser.objects.get(user__username = restid)
    if request.GET.get('submit')=='Rate':
        menuid    =  request.GET.get('menuid')
        val    =  request.GET.get('rate')
        instance = Menu.objects.get(id=menuid)
        n=instance.no_of_rated
        rating = instance.rating
        instance.rating=(n*rating+int(val))//(n+1)
        instance.no_of_rated = n+1
        instance.save()
        print(instance.rating,instance.no_of_rated)
        return redirect('UserMenu',restid)
    return render(request,'menu/ratings.html',context={'Menu':menu,'rest_user':rest_user})




@api_view(['GET'])
def MenuApi(request,restid):
    if request.method == 'GET' :
        menu = Menu.objects.filter(r_id__user__username = restid).order_by('-rating')
        serializer = MenuSerialiser(menu,many = True)
        return Response(serializer.data )
    return JsonResponse(serializer.errors,status=400)

@api_view(['GET'])
def TopRatedFood(request,sub_zone):
    if request.method == 'GET' :
        menu = Menu.objects.filter(r_id__sub_zone = sub_zone,rating__gte=3).order_by('-rating')
        serializer = MenuSerialiser(menu,many = True)
        return Response(serializer.data )
    return JsonResponse(serializer.errors,status=400)