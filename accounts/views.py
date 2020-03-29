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
        test1 = User(
            user_name=request.POST.get('user_name'),
            password=request.POST.get("password"),
        )
        test1.save()
        return HttpResponse("<p>用户添加成功！</p>")


@csrf_exempt
def delete(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        nameIndb = User.objects.filter(user_name=user_name).first()
        if nameIndb:
            nameIndb.delete()
            return HttpResponse(f'<p>{user_name}删除成功!</p>')
        else:
            return HttpResponse('<p>输入有误,用户不存在')


@csrf_exempt
def change(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nameIndb = User.objects.filter(id=id).first()
        if nameIndb:
            nameIndb.user_name = request.POST.get('user_name')
            nameIndb.password = request.POST.get('password')
            nameIndb.save()
            return HttpResponse(f'<p>{nameIndb.user_name}修改成功!</p>')
        else:
            return HttpResponse(f'<p>输入有误,{nameIndb.user_name}不存在')


@csrf_exempt
def select(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        nameIndb = User.objects.filter(user_name=user_name)
        if nameIndb:
            isdict = serializers.serialize('json', nameIndb)
            return JsonResponse(isdict, safe=False)
        else:
            return HttpResponse(f'<p>输入有误,{user_name}不存在')
