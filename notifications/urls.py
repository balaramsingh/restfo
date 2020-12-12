from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('notifications/',views.notifications,name='notification'),

    path('notifications/delete/<int:notification_id>/', views.delete_notification),

    path('loggedin_a/',views.loggedin_a),
    path('loggedin_g/',views.loggedin_g),
    path('loggedin_o/',views.loggedin_o),
    path('loggedin_p/',views.loggedin_p),

    path('notifications/show_app/<int:notification_id>/', views.show_app),
    path('notifications/show_gen/<int:notification_id>/', views.show_gen),
    path('notifications/show_ord/<int:notification_id>/', views.show_ord),
    path('notifications/show_pay/<int:notification_id>/', views.show_pay),

    path('profiles/<str:usrname>/notifications/give_g_notification/', views.give_g_notification, name='give-general-notification'),
    path('profiles/<str:usrname>/notifications/give_g_notification/give_g/', views.give_g),

    path('profiles/<str:usrname>/notifications/give_o_notification/', views.give_o_notification, name='give-order-notification'),
    path('profiles/<str:usrname>/notifications/give_o_notification/give_o/', views.give_o),

    path('profiles/<str:usrname>/notifications/give_p_notification/', views.give_p_notification, name='give-payment-notification'),
    path('profiles/<str:usrname>/notifications/give_p_notification/give_p/', views.give_p),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
