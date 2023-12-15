from django.urls import path,include
from . import  views
urlpatterns = [
    path('',views.index,name='index'),
    path('test222222222',views.test,name='test'),
     path('test2222222222222',views.test,name='test'),
]
