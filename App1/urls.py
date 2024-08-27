from django.urls import path
from App1 import views
urlpatterns=[
    # path('',views.fun,name='home'),
    path('cars',views.cars,name='car'),
    path('',views.movies,name='mov'),
    path('movies/<int:rid>',views.single,name='single')
]