from django.urls import path,include
from . import  views
urlpatterns = [
    path('',views.index,name='index'),
    path('test',views.test,name='test'),
    path('test2',views.test,name='test'),
]
