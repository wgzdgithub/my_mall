from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from mall.models import Product


@csrf_exempt
def add(request):
    if request.method == 'POST':
        test1 = Product(
            name=request.POST.get('name'),
            price=request.POST.get("price"),
            category=request.POST.get("category"),
        )
        test1.save()
        return HttpResponse("<p>商品添加成功！</p>")
    else:
        return HttpResponse("<p>商品添加失败</p>")


@csrf_exempt
def delete(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        nameIndb = Product.objects.filter(uid=uid).first()
        if nameIndb:
            nameIndb.delete()
            return HttpResponse(f'<p>{uid}删除成功!</p>')
        else:
            return HttpResponse('<p>输入有误,商品不存在')


@csrf_exempt
def change(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        nameIndb = Product.objects.filter(uid=uid).first()
        if nameIndb:
            nameIndb.name = request.POST.get('name')
            nameIndb.price = request.POST.get('price')
            nameIndb.category = request.POST.get('category')
            nameIndb.save()
            return HttpResponse(f'<p>{uid}修改成功!</p>')
        else:
            return HttpResponse(f'<p>输入有误,{uid}不存在')


@csrf_exempt
def select(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        nameIndb = Product.objects.filter(uid=uid)
        if nameIndb:
            isdict = serializers.serialize('json', nameIndb)
            return JsonResponse(isdict, safe=False)
        else:
            return HttpResponse(f'<p>输入有误,{uid}不存在')
