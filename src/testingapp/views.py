from django.http import HttpResponse
from django.shortcuts import render

from testingapp.models import Country


def get_country(request, *args, **kwargs):
    obj = Country.objects.get(id=1)
    print(obj)
    return HttpResponse("<h1>Hello World</h1>")
