from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Seller
from Sellerapp . models import *
from django.template import loader

# Create your views here.

def seller_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        datas = Seller.objects.filter(email=email, password=password)
        if datas:
            request.session['seller_id'] = email
            print('login successfully...!')
            return redirect('/seller')

        else:
            return HttpResponse('Please enter a valid email id')
    return render(request, 'seller-login.html')


def seller_signup(request):
    if request.method == 'POST':
        seller_name = request.POST.get('seller_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        experience = request.POST.get('experience')
        license_number = request.POST.get('license_number')
        password = request.POST.get('password')
        print(seller_name, email, phone_number, experience, license_number, password)
        data = Seller()
        data.seller_name = seller_name
        data.email = email
        data.phone_number = phone_number
        data.experience = experience
        data.license_number = license_number
        data.password = password
        data.save()
        return redirect('/seller/seller_login')
    else:
        return render(request,'seller-signup.html')

def seller_home(request):
    if 'seller_id' in request.session:
        data = request.session['seller_id']
        data1 = Seller.objects.filter(email=data)
        print(data1.values())
        return render(request, 'seller-home.html', {'data': data1})
    else:
        return redirect('/seller/seller_login')


def seller_addproduct(request):
    if request.method == 'POST':
        data = Product()
        data.product_id = request.POST.get('product_id')
        data.main_category_id = request.POST.get('main_category_id')
        data.product_name = request.POST.get('product_name')
        data.price = request.POST.get('price')
        data.description = request.POST.get('description')
        data.expiry_date = request.POST.get('expiry_date')
        data.quantity = request.POST.get('quantity')
        data.brand_id = request.POST.get('brand_id')
        data.save()
        print("product add successfully...........")
        return redirect('/seller')
    else:
        return render(request,'seller-addproduct.html')

def seller_editproduct(request,product_id):
    if request.method == 'POST':
        data = Product.objects.get(product_id=product_id)
        data.seller_id = request.POST.get('seller_id')
        data.product_id = request.POST.get('product_id')
        data.main_category_id = request.POST.get('main_category_id')
        data.product_name = request.POST.get('product_name')
        data.price = request.POST.get('price')
        data.description = request.POST.get('description')
        data.expiry_date = request.POST.get('expiry_date')
        data.quantity = request.POST.get('quantity')
        data.brand_id = request.POST.get('brand_id')
        data.save()
        print("product add successfully...........")
        return redirect('/seller')
    else:
        data = Product.objects.filter(product_id=product_id)
        return render(request, 'seller-editproduct.html', {'data': data})

def seller_viewproduct(request):
    print('Product Function called')
    if 'seller_id' in request.session:
        data = Product.objects.filter(seller_id=Seller.objects.get(email=request.session['seller_id']))
        # data1 = Category.objects.filter(product_id=Product.objects.get(product_id= request.POST.get('product_id')))
        return render(request, 'seller-viewproduct.html', {'data': data})
    else:
        return redirect('/seller/seller_login')

def seller_deleteproduct(request, product_id):
    data = Product.objects.get(product_id=product_id)
    data.delete()
    return redirect('/seller')

def seller_add_image(request, product_id):
    if 'seller_id' in request.session:
        product = Product.objects.filter(product_id=product_id)
        if request.method == 'POST':
            seller_id = request.session('seller_id', None)
            image = request.FILES.get('image')
            print('hiiiiiiiiiii')
            data = ProductImage()
            data.image = image
            data.seller_id = Seller.objects.get(seller_id=seller_id)
            data.product_id = Product.objects.get(product_id=product_id)
            data.save()
            return redirect('/seller')
        return render(request, 'seller-productimage.html',{'product':product})
    else:
        return render(request,'seller-login.html')

# def seller_edit_image(request,product_id):
#     if request.method == 'POST':
#         data = Product.objects.get(product_id=product_id)
#         image = request.FILES.get('image')
#         data.image = image
#         data.save()
#         return redirect('/seller')
#     else:
#         data = Product.objects.filter(product_id=product_id)
#         return render(request,'seller-editproduct.html')



def seller_logout(request):
    del request.session['seller_id']
    return redirect('/seller/seller_login')