from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404, HttpResponse
import json
import datetime

from django.views.generic import ListView

from .forms import *
from .models import *
from .utils import cartData, guestOrder


def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    new_products = Product.objects.filter(tag = 'new')[:4]
    best_products = Product.objects.filter(tag = 'best')[:4]

    #paginator = Paginator(products,6)

    #page_number = request.GET.get('page')
    #page_obj = paginator.get_page(page_number)

    context = {'new_products': new_products,
               'best_products': best_products,
               'cartItems': cartItems,
               'order': order,
               }
    return render(request, 'store/home.html',context)


def show_category(request):
    data = cartData(request)
    cats = Category.objects.all()

    filter_cats = [int(item) for item in request.GET.getlist('cat')]

    if (request.GET.get('price_min') == None) and (request.GET.get('price_max') == None):
        price_min, price_max = 0, 1000
    else:
        price_min, price_max = request.GET.get('price_min'), request.GET.get('price_max')
    if len(request.GET.getlist('cat')) == 0:
        products = Product.objects.filter(price__range=(price_min, price_max))
    else:
        products = Product.objects.filter(cat__in = request.GET.getlist('cat'), price__range=(price_min, price_max))
    order = data['order']

    if request.GET.get('text_search'):
        search_text = request.GET.get('text_search').lower()
        products = []
        for i in Product.objects.all():
            if search_text in i.name.lower():
                products.append(i)
            elif search_text in i.about:
                products.append(i)
            else:
                for c in i.cat.all():
                    if search_text == c.name.lower():
                        products.append(i)
    paginator = Paginator(products, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'products': products,
               'cats': cats,
               'cat_selected': 0,
               'order': order,
               'page_obj': page_obj,
               'price_min': price_min,
               'price_max': price_max,
               'filter_cats': filter_cats
               }
    return render(request, 'store/categories.html', context)


def post(request, id_product):
    data = cartData(request)
    cartItems = data['cartItems']
    product = Product.objects.get(id=id_product)
    order = data['order']
    context = {'product': product,
               'title': product.name,
               'order': order,
               'cartItems': cartItems,
               }
    return render(request, 'store/product.html', context)


def order(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items'].order_by('id')
    context = {
               'title': 'checkout',
               'cartItems': cartItems,
               'order': order,
               'items': items,
               }
    return render(request, 'store/order.html',context)


def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        customer, order = guestOrder(request,data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == float(order.get_cart_total):
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse("Payment complete!", safe=False)

def register(response):
    cats = Category.objects.all()
    if response.method == 'POST':
        form = RegisterUserForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegisterUserForm()

    return render(response, 'store/register.html', {'form': form, 'cats': cats, 'title': 'register'})

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'store/login.html'
