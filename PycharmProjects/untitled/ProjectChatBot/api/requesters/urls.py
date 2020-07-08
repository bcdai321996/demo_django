from django.urls import path
from . import views

urlpatterns = [
    path('requester/get_requester', views.get_requester)

]

