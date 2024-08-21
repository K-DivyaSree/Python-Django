from django.urls import path
from App1 import views

urlpatterns = [
    path('<str:state>/<str:festival>/', views.festival_wishes, name='festival_wishes'),
]
