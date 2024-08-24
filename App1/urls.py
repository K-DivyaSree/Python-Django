from django.urls import path
from App1 import views
urlpatterns=[
    # path('',views.fun,name='home'),
    path('',views.cars,name='car')
]