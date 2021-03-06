from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.views.decorators.csrf import csrf_protect

from accounts.models import User


@csrf_exempt
def add(request):
    if request.method == 'POST':
        try:
            test1 = User(
                user_name=request.POST.get('user_name'),
                password=request.POST.get("password"),
            )
            test1.save()
            data = User.objects.filter(user_name=request.POST.get("user_name"))
            isdict = serializers.serialize('json', data)
            return JsonResponse(isdict, safe=False)
        except:
            return JsonResponse({"code": 404})
    else:
        return JsonResponse({"code": 404})


@csrf_exempt
def delete(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            nameIndb = User.objects.filter(id=id)
            isdict = serializers.serialize('json', nameIndb)
            if nameIndb:
                nameIndb.delete()
                return JsonResponse(isdict, safe=False)
        except:
            JsonResponse({"code": 404})
    else:
        return JsonResponse({"code": 404})


@csrf_exempt
def change(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            nameIndb = User.objects.filter(id=id).first()
            if nameIndb:
                nameIndb.user_name = request.POST.get('user_name')
                nameIndb.password = request.POST.get('password')
                nameIndb.save()
                data = User.objects.filter(id=id)
                isdict = serializers.serialize('json', data)
                return JsonResponse(isdict, safe=False)
        except:
            return JsonResponse({"code": 404})
    else:
        return JsonResponse({"code": 404})


@csrf_exempt
def select(request):
    if request.method == 'GET':
        try:
            id = request.GET.get('id')
            data = User.objects.filter(id=id)
            if data:
                isdict = serializers.serialize('json', data)
                return JsonResponse(isdict, safe=False)
        except:
            return JsonResponse({"code": 404})
    else:
        return JsonResponse({"code": 404})
