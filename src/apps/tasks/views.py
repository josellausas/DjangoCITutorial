from django.shortcuts import render
from django.http import HttpResponse

# The index view
def index(request):
    response = "<p>Hola Mundo!</p>"
    return HttpResponse(response)
