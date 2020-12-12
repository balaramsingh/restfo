from django.urls import path,include
from .views import profile_view,check_view,check_view2,time_slot,api_view1,api_view2,give_review,show,ReviewAPI

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('profiles/<str:username>/',profile_view,name='profiles'),
    path('login/restaurant/profiles/<str:username>/',profile_view),
    path('profiles/<str:username>/check',check_view),
    path('profiles/<str:username>/check2',check_view2),
    path('login/restaurant/profiles/<str:username>/check',check_view),
    path('login/restaurant/profiles/<str:username>/check2',check_view2),
    path('api_check_tables/<str:username>/<str:date_api>/<int:slot_no>/',api_view1),
    path('api_check_slots/<str:username>/<str:date_api>/<int:table_size>/',api_view2),
    path('time_slot/',time_slot),

    path('profiles/<str:username>/give_rev/',give_review),
    path('profiles/<str:username>/show_rev/',show,name="show"),
    path('login/restaurant/profiles/<str:username>/give_rev/',give_review),
    path('login/restaurant/profiles/<str:username>/show_rev/',show,name="show"),
    path('rest_review/<str:username>',ReviewAPI)

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
