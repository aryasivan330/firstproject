from django.urls import path
from .import views
urlpatterns=[
    path('',views.hello,name='hello'),
    path('welcome',views.welcome,name='welcome'),
    path('hai',views.hai,name='hai'),

]
