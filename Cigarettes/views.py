from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from Cigarettes.serializer import *


def mainPage(request):
    return render(request, 'Mainpage.html')


@api_view(['GET'])
@permission_classes([AllowAny])
def getCart(request):
    chat_id_req = request.query_params['chat_id']
    check_id = ModelCart.objects.filter(chat_id=chat_id_req).values()
    check_id = str(check_id)
    if chat_id_req in check_id:
        instance = ModelCart.objects.filter(chat_id=chat_id_req).values()
        serializer = CartSerializer(data=request.data, instance=instance)
        serializer.is_valid()
        return Response(instance)
    else:
        return Response({'getCart_ERROR:ID не найден'})


@api_view(['GET'])
@permission_classes([AllowAny])
def getBrands(request):
    brand = request.query_params['brand']
    check_id = ModelProduct.objects.filter(brand=brand).values()
    check_id = str(check_id)
    if brand in check_id:
        instance = ModelProduct.objects.filter(brand=brand).values()
        serializer = ProductSerializer(data=request.data, instance=instance)
        serializer.is_valid()
        return Response(instance)
    else:
        return Response({'getBrand_ERROR:ID не найден'})


@api_view(['GET'])
@permission_classes([AllowAny])
def clearCart(request, **kwargs):
    chat_id_req = request.query_params['chat_id']
    check_id = ModelCart.objects.filter(chat_id=chat_id_req).values()
    check_id = str(check_id)
    if chat_id_req in check_id:
        instance = ModelCart.objects.filter(chat_id=chat_id_req).delete()
        serializer = CartSerializer(data=request.data, instance=instance)
        serializer.is_valid()
        print(str(check_id))
        return Response({'DELETE': f'Запись удалена {check_id}'})
    else:
        return Response({'clearCart_ERROR:ID не найден'})


@api_view(['GET'])
@permission_classes([AllowAny])
def editCart(request):
    product = request.query_params['product_id']
    chat_id = request.query_params['chat_id']
    quantity_req = request.query_params['quantity']
    try:
        _ = ModelCart.objects.filter(chat_id=chat_id).values('chat_id')[0]
    except IndexError:
        return Response({'Exception': 'Chat ID does not Exist'})
    same_rec = ModelCart.objects.filter(chat_id=chat_id)
    if quantity_req == "0":
        _ = ModelCart.objects.filter(chat_id=chat_id).delete()
        return Response({})
    if not same_rec.exists():
        try:
            a = ModelCart(quantity=int(quantity_req), chat_id=int(chat_id),
                          product=ModelProduct.objects.get(id=product))
        except ModelProduct.DoesNotExist:
            return Response({"Exception": "ID not found in catalogue"}, status=status.HTTP_404_NOT_FOUND)
        a.save()
        a = ModelCart.objects.get(id=a.id)
        serializer = CartSerializer(data={'chat_id': chat_id, 'quantity': quantity_req, 'product': product},
                                    instance=a)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        else:
            return Response({'Exception': 'Data invalid'})
        return Response(serializer.data)
    else:
        a = same_rec[0]
        same_rec[0].quantity = quantity_req
        a.save()
        serializer = CartSerializer(data={'chat_id': chat_id, 'quantity': quantity_req, 'product': product},
                                    instance=a)
        print(request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        else:
            return Response({'Exception': 'Data invalid'})
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def getProducts(request):
    id = request.query_params['id']
    name = request.query_params['name']
    brand = request.query_params['brand']
    brand_check = ModelProduct.objects.filter(brand=brand).values()
    id_check = ModelProduct.objects.filter(id=id).values()
    name_check = ModelProduct.objects.filter(name=name).values()
    if name in str(name_check) and brand in str(brand_check) and id in str(id_check):
        instance = ModelProduct.objects.filter(name=name, id=id, brand=brand).values()
        serializer = CartSerializer(data=request.data, instance=instance)
        serializer.is_valid()
        return Response(instance)
    else:
        return Response({'getProduct_ERROR:ID не найден'})


@api_view(['GET'])
@permission_classes([AllowAny])
def addToCart(request):
    id_req = request.query_params['id']
    chat_id = request.query_params['chat_id']
    quantity_req = (request.query_params['quantity'] if 'quantity' in request.query_params else 1)
    same_rec = ModelCart.objects.filter(product=id_req, chat_id=chat_id)
    if same_rec.exists():
        print(f'found same record {same_rec.values()}')
        quantity_req = same_rec[0].quantity + int(quantity_req)
        a = same_rec[0]
        a.quantity = quantity_req
        a.save()
    else:
        try:
            a = ModelCart(quantity=int(quantity_req), chat_id=int(chat_id), product=ModelProduct.objects.get(id=id_req))
        except ModelProduct.DoesNotExist:
            return Response({"Exception": "ID not found in catalogue"}, status=status.HTTP_404_NOT_FOUND)
        a.save()
    a = ModelCart.objects.get(id=a.id)
    serializer = CartSerializer(data={'chat_id': chat_id, 'quantity': quantity_req, 'product': id_req}, instance=a)
    print(request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    else:
        return Response({'Exception': 'Data invalid'})
    return Response(serializer.data)


# @api_view(['GET'])
# @permission_classes([AllowAny])
# def addItem(request):

