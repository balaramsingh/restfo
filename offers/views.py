from django.shortcuts import render
from .models import Coupon
from django.contrib.auth.decorators import login_required
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .serializers import CouponSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import JsonResponse

from datetime import datetime
import pytz
utc=pytz.UTC

def coupon_show(request,username):
    offers = Coupon.objects.filter(restname=username)

    context = {
    'offers' : offers
    }

    return render(request, 'offers/show_offers.html', context)

@login_required
def create_coupon(request):
    if request.method=="POST":
        restname = request.user.username
        title = request.POST.get('title')
        code = request.POST.get('code')
        valid_from = request.POST.get('valid_from')
        valid_to = request.POST.get('valid_to')
        discount = int(request.POST.get('discount'))
        applicable = request.POST.get('applicable')
        x = Coupon(restname=restname,title=title,code=code,valid_from=valid_from,valid_to=valid_to,discount=discount,applicable=applicable)
        x.save()
        return render(request, 'offers/create_offer.html')
    else:
        return render(request, 'offers/create_offer.html')

@csrf_exempt
@api_view(['GET'])
def api_offers(request,username):
    if request.method == 'GET' :
        obj = Coupon.objects.filter(restname=username,valid_from__lte=datetime.now(), valid_to__gte=datetime.now())
        serializer = CouponSerializer(obj,many=True)
        return JsonResponse(serializer.data , safe=False)

        
