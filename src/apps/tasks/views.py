from django.shortcuts import render
from django.http import HttpResponse

# The index view
def index(request):
    response = "<html><p>Hola Mundo!</p></html>"
    return HttpResponse(response)

def detail(request, task_id):
    response = "<html><p>A list goes here</p></html>"
    return HttpResponse(response)
