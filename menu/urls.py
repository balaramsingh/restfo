from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('menu',views.menuview,name='menu_view'),
    path('menu_update/<str:menuid>',views.update,name='menu_update'),
    path('MenuOrders',views.OrderConfirm,name='MenuOrder'),
    path('UserMenu/<str:restid>',views.User_Menu,name="UserMenu"),
    path('MenuRating/<str:restid>',views.rating,name="MenuRating"),
    path('menuapi/<str:restid>',views.MenuApi),
    path('ToFoodApi/<str:sub_zone>',views.TopRatedFood)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)