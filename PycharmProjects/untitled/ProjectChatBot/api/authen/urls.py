from django.urls import path
from . import views

urlpatterns = [
    path('authen/login_requester', views.login_requester),
    path('authen/logout', views.logout_requester)

]

