from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from mine.models import Cart, Order


@csrf_exempt
def cart_add(request):
    if request.method == 'POST':
        test1 = Cart(
            order_id=request.POST.get('order_id'),
            goods_id=request.POST.get("goods_id"),
            goods_num=request.POST.get("goods_num"),
        )
        test1.save()
        return HttpResponse("<p>添加成功！</p>")
    else:
        return HttpResponse("<p>添加失败</p>")


@csrf_exempt
def cart_delete(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        nameIndb = Cart.objects.filter(order_id=order_id).first()
        if nameIndb:
            nameIndb.delete()
            return HttpResponse(f'<p>{order_id}删除成功!</p>')
        else:
            return HttpResponse('<p>输入有误,商品不存在')


@csrf_exempt
def cart_change(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nameIndb = Cart.objects.filter(id=id).first()
        if nameIndb:
            nameIndb.order_id = request.POST.get('order_id')
            nameIndb.goods_id = request.POST.get('goods_id')
            nameIndb.goods_num = request.POST.get('goods_num')
            nameIndb.save()
            return HttpResponse(f'<p>{id}修改成功!</p>')
        else:
            return HttpResponse(f'<p>输入有误,{id}不存在')


@csrf_exempt
def cart_select(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        nameIndb = Cart.objects.filter(order_id=order_id)
        if nameIndb:
            isdict = serializers.serialize('json', nameIndb)
            return JsonResponse(isdict, safe=False)
        else:
            return HttpResponse(f'<p>输入有误,{order_id}不存在</p>')


@csrf_exempt
def order_add(request):
    if request.method == 'POST':
        test1 = Order(
            order_id=request.POST.get('order_id'),
            user_id=request.POST.get("user_id"),
            status=request.POST.get("status"),
            order_time=request.POST.get("order_time"),
        )
        test1.save()
        return HttpResponse("<p>订单添加成功！</p>")
    else:
        return HttpResponse("<p>订单添加失败</p>")


@csrf_exempt
def order_delete(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        nameIndb = Order.objects.filter(order_id=order_id).first()
        if nameIndb:
            nameIndb.delete()
            return HttpResponse(f'<p>{order_id}删除成功!</p>')
        else:
            return HttpResponse('<p>输入有误,订单不存在')


@csrf_exempt
def order_change(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        nameIndb = Order.objects.filter(order_id=order_id).first()
        if nameIndb:
            nameIndb.order_id = request.POST.get('order_id')
            nameIndb.user_id = request.POST.get('user_id')
            nameIndb.status = request.POST.get('status')
            nameIndb.order_time = request.POST.get('order_time')
            nameIndb.save()
            return HttpResponse(f'<p>{order_id}修改成功!</p>')
        else:
            return HttpResponse(f'<p>输入有误,{order_id}不存在')


@csrf_exempt
def order_select(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        nameIndb = Order.objects.filter(order_id=order_id).first()
        if nameIndb:
            isdict = serializers.serialize('json', nameIndb)
            return JsonResponse(isdict, safe=False)
        else:
            return HttpResponse(f'<p>输入有误,{order_id}不存在')
