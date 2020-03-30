from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from mall.models import Product


@csrf_exempt
def add(request):
    if request.method == 'POST':
        try:
            test1 = Product(
                name=request.POST.get('name'),
                price=request.POST.get("price"),
                category=request.POST.get("category"),
            )
            test1.save()
            data = Product.objects.filter(name=request.POST.get("name"))
            isdict = serializers.serialize('json', data)
            return JsonResponse(isdict, safe=False)
        except:
            return HttpResponse("<p>商品添加失败</p>")
    else:
        return HttpResponse("<p>请求错误</p>")


@csrf_exempt
def delete(request):
    if request.method == 'POST':
        try:
            uid = request.POST.get('uid')
            data = Product.objects.filter(uid=uid)
            isdict = serializers.serialize('json', data)
            if data:
                data.delete()
                return JsonResponse(isdict, safe=False)
        except:
            return HttpResponse('<p>输入有误</p>')
        else:
            return HttpResponse('<p>请求错误</p>')


@csrf_exempt
def change(request):
    if request.method == 'POST':
        try:
            uid = request.POST.get('uid')
            nameIndb = Product.objects.filter(uid=uid).first()
            if nameIndb:
                nameIndb.name = request.POST.get('name')
                nameIndb.price = request.POST.get('price')
                nameIndb.category = request.POST.get('category')
                nameIndb.save()
                data = Product.objects.filter(uid=uid)
                isdict = serializers.serialize('json', data)
                return JsonResponse(isdict, safe=False)
        except:
            return HttpResponse(f'<p>输入错误</p>')
    else:
        return HttpResponse(f'<p>请求错误</p>')


@csrf_exempt
def select(request):
    if request.method == 'GET':
        uid = request.GET.get('uid')
        nameIndb = Product.objects.filter(uid=uid)
        if nameIndb:
            isdict = serializers.serialize('json', nameIndb)
            return JsonResponse(isdict, safe=False)
        else:
            return HttpResponse(f'<p>输入有误,{uid}不存在')
