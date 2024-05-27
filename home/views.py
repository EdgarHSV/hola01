from django.http import HttpResponse
from django.shortcuts import render     # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/

def homeView(request):
    context = {
        'message': 'This message taken from "context" in "homeView" with HTML template.'
    }
    return render(request, "home/index.html", context)

def startpageView(request):
    context = {
        'message': 'This message taken from "context" in "startpageView" with HTML template.'
    }
    return render(request, "home/startpage.html", context)

def rootView(request):
    output= 'App start... How is it going Shaman!<br/><br/>'
    output += '- Hello from "rootView" from "rootView" function template (no context or HTML template).'
    return HttpResponse(output)
