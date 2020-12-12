from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('nearbyrest', views.NearByRestaurants,name="near"),
    path('rest_list/<str:restid>',views.lister,name="rest_list")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)