from django.contrib import admin
from django.urls import path

from FRM import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('dashboard', views.dashboard, name = "dashboard"),
    path('signup', views.signup, name = 'signup'),
    path('forgotpassword', views.forgotpassword, name = 'forgotpassword'),
    path('transactionreport', views.transactionreport, name = 'transactionreport'),
    path('logout', views.logout_view, name='logout'),
    path('rules_creation', views.rules_creation_view, name='rules_creation'),
    path('rules_list', views.rules_list_view, name='rules_list')
]