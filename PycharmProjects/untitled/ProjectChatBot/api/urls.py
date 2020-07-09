from django.urls import path, include

urlpatterns = [
    path('api/', include('api.requesters.urls')),
    path('api/', include('api.authen.urls')),

]
