from django.shortcuts import render
#Класс HttpResponse - для одиночного запроса
from django.http import HttpResponse

def hello_view(req):
    if req.method == "GET":
        return HttpResponse('Hello World!')

def emodji(req):
    if req.method == "GET":
        return HttpResponse("😁😅🥰😱🤕😵‍💫")

def pic(req):
    if req.method == 'GET':
        return HttpResponse('<img src="https://i.pinimg.com/736x/70/5b/bb/705bbb820c7332b04d619f7536645753.jpg">')
    