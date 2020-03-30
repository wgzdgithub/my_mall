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
        data = Cart.objects.filter(goods_id=request.POST.get("goods_id"))
        isdict = serializers.serialize('json', data)
        return JsonResponse(isdict, safe=False)
    else:
        return HttpResponse("<p>添加失败</p>")


@csrf_exempt
def cart_delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nameindb = Cart.objects.filter(id=id)
        isdict = serializers.serialize('json', nameindb)
        if nameindb:
            nameindb.delete()
            return JsonResponse(isdict, safe=False)
        else:
            return HttpResponse('<p>输入有误,商品不存在')


@csrf_exempt
def cart_change(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            nameIndb = Cart.objects.filter(id=id).first()
            if nameIndb:
                nameIndb.order_id = request.POST.get('order_id')
                nameIndb.goods_id = request.POST.get('goods_id')
                nameIndb.goods_num = request.POST.get('goods_num')
                nameIndb.save()
                data = Cart.objects.filter(id=id)
                isdict = serializers.serialize('json', data)
                return JsonResponse(isdict, safe=False)
        except:
            return HttpResponse(f'<p>输入错误</p>')
    else:
        return HttpResponse(f'<p>请求错误</p>')


@csrf_exempt
def cart_select(request):
    if request.method == 'GET':
        try:
            id = request.GET.get('id')
            nameindb = Cart.objects.filter(id=id)
            if nameindb:
                isdict = serializers.serialize('json', nameindb)
                return JsonResponse(isdict, safe=False)
        except:
            return HttpResponse(f'<p>输入错误</p>')
    else:
        return HttpResponse(f'<p>请求错误</p>')


@csrf_exempt
def order_add(request):
    if request.method == 'POST':
        try:
            test1 = Order(
                order_id=request.POST.get('order_id'),
                user_id=request.POST.get("user_id"),
                status=request.POST.get("status"),
                order_time=request.POST.get("order_time"),
            )
            test1.save()
            data = Order.objects.filter(order_id=request.POST.get("order_id"))
            isdict = serializers.serialize('json', data)
            return JsonResponse(isdict, safe=False)
        except:
            return HttpResponse("<p>输入错误</p>")
    else:
        return HttpResponse("<p>请求错误</p>")


@csrf_exempt
def order_delete(request):
    if request.method == 'POST':
        try:
            order_id = request.POST.get('order_id')
            nameindb = Order.objects.filter(order_id=order_id)
            isdict = serializers.serialize('json', nameindb)
            if nameindb:
                nameindb.delete()
                return JsonResponse(isdict, safe=False)
        except:
            return HttpResponse('<p>输入错误 </p>')
    else:
        return HttpResponse('<p>请求错误</p>')


@csrf_exempt
def order_change(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            nameindb = Order.objects.filter(id=id).first()
            if nameindb:
                nameindb.order_id = request.POST.get('order_id')
                nameindb.user_id = request.POST.get('user_id')
                nameindb.status = request.POST.get('status')
                nameindb.save()
                data = Order.objects.filter(id=id)
                isdict = serializers.serialize('json', data)
                return JsonResponse(isdict, safe=False)
        except:
            return HttpResponse(f'<p>输入有误</p>')
    else:
        return HttpResponse(f'<p>请求错误</p>')


@csrf_exempt
def order_select(request):
    if request.method == 'GET':
        try:
            order_id = request.GET.get('order_id')
            nameindb = Order.objects.filter(order_id=order_id)
            if nameindb:
                isdict = serializers.serialize('json', nameindb)
                return JsonResponse(isdict, safe=False)
        except:
            return HttpResponse(f'<p>输入有误</p>')
    else:
        return HttpResponse(f'<p>请求错误</p>')
