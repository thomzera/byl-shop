from django.http import HttpResponse

# from django.shortcuts import render


def index(requet):
    return HttpResponse('INDEX PAGE')
