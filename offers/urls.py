from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from .views import coupon_show, create_coupon, api_offers

urlpatterns = [

    path('profiles/<str:username>/view_offers/',coupon_show),
    path('login/restaurant/profiles/<str:username>/view_offers/',coupon_show),
    path('create_coupon/',create_coupon),
    path('api_offers/<str:username>/',api_offers)

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
