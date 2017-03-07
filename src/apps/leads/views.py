from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# The index view
def index(request):
    response = "<html><p>Hola Mundo!</p></html>"
    return HttpResponse(response)
