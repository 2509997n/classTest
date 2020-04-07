from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world.  You're at the news index.")


def detail(request, headline_id):
    return HttpResponse("You're looking at headline %s." % headline_id)


def results(request, headline_id):
    response = "You're looking at the results of headline %s."
    return HttpResponse(response % headline_id)


def vote(request, headline_id):
    return HttpResponse("You're voting on headline %s." % headline_id)
