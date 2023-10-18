from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(response):
    return HttpResponse('Hello word');
def test(response):
    return HttpResponse('test');