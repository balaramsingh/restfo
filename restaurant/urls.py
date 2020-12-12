from django.urls import path
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.main,name='main'),
    path('register/',views.Signup,name='register'),
    path('register/customer_register/',views.customer_register.as_view(),name='customer_register'),
    path('register/restaurant_register/',views.restaurant_register.as_view(),name='restaurant_register'),
    path('login/',views.login_request, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('api/',views.restaurant_view),
    path('login/restaurant/homepage.html',views.mainhome,name='cust'),
    path('login/restaurant/resthomepage.html',views.resthome,name='rest'),

    path('login/restaurant/tables/',views.tables),


     path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="restaurant/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="restaurant/password_reset_sent.html"),
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="restaurant/password_reset_form.html"),
     name="password_reset_confirm"),

    path('reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name="restaurant/password_reset_done.html"),
        name="password_reset_complete"),

    path('index/',views.index,name="index"),
    path('charge/',views.charge,name="charge"),
    path('success/<str:args>/',views.successMsg,name="success"),

    path('index2/',views.index2,name="index2"),
    path('charge2/',views.charge2,name="charge2"),
    path('success2/<str:args>/',views.successMsg2,name="success2"),

    path('UserMenu/<str:username>/index3/<str:cost>/',views.index3,name="index3"),
    path('UserMenu/<str:username>/charge3/<str:cost>/',views.charge3,name="charge3"),

    path('UserMenu/<str:username>/success3/<str:args>/',views.success3,name="success3"),

]
