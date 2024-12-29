from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('This is index page')