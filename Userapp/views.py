from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Product, Cart, ReviewRating, Category, UserImage
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.template import loader
from Sellerapp.models import *
from Userapp.models import *
from Adminapp.models import *
from Userapp.models import UserAddress
from django.db.models import Q, Sum, F
from decimal import Decimal


def home_page(request):
    data = Product.objects.select_related('seller_id').prefetch_related('images').all()
    cat = Category.objects.all()
    categorized_products = {}
    for y in cat:
        category_products = data.filter(main_category_id=y.main_category_id)
        if category_products.exists():
            categorized_products[y.main_category_name] = category_products
    print(data.values())
    users='no user'
    if 'user' in request.session:
        current_user = request.session['user']
        users=User.objects.get(email=current_user)

    return render(request, 'homepage.html',{'products': data,'user':users, 'cat': cat, 'categorized_products': categorized_products})


def products(request, id):
    print("dcfvgbhnjm")
    data = Product.objects.select_related('seller_id').prefetch_related('images').filter(product_id=id)
    datas = ReviewRating.objects.filter(product_id=Product.objects.get(product_id=id))
    if 'user' in request.session:
        print("sdfghjvbnhj")
        email = request.session.get('user')
        print(data.values())
        print(f'user : {email}')
        if request.method == 'POST':
            print('cart now')
            quantity = request.POST.get('quantity')
            cart_data = Cart()
            cart_data.product_id = Product.objects.get(product_id=id)
            cart_data.quantity = quantity
            cart_data.user_id = User.objects.get(email=email)
            cart_data.save()
            return redirect('/cart')
    return render(request, 'single-product.html', {'products': data, 'review': data})


def cart(request):
    print("sdfghj")
    if 'user' in request.session:
        print("aaaaaaaaaaaaaaaaaaaaaa")
        email = request.session.get('user')
        data = Cart.objects.filter(user_id=User.objects.get(email=email))
        print(data.values())
        # total_price = Cart.objects.filter(user_id=User.objects.get(email=request.session['user'])).aggregate(
        #     total_price=Sum(F('product_id__price') * F('quantity'), output_field=models.DecimalField())
        # )['total_price'] or Decimal('0.00')
        # print(f"Total price for user : ₹{total_price}")
        return render(request, 'cart.html', {'cart': data})
    else:
        return redirect('/login')


def dlt_product(request, cart_id):
    print("rtttttttttttttttttttttttttttttt")
    data = Cart.objects.get(cart_id=cart_id)
    data.delete()
    return redirect('/cart')


def category(request, main_category_id):
    print(main_category_id)
    print("category function")
    data = Category.objects.get(main_category_id=main_category_id)
    print(data)
    data1 = Product.objects.filter(main_category_id=data)
    print(data1.values())
    if request.method == 'POST':
        sort_price = request.POST.get('sort_price')
        sort_discount = request.POST.get('sort_discount')
        sort_relevance = request.POST.get('sort_relevance')
        if sort_price == 'low_to_high':
            data1 = data1.order_by('price')
        elif sort_price == 'high_to_low':
            data1 = data1.order_by('-price')
        elif sort_relevance:
            print('qqqqqqq')
            data1 = data1.prefetch_related('images')

    return render(request, 'category.html', {'cat': data1})


def search(request):
    print("rrrrrrrrr")
    data = Product.objects.select_related('seller_id').prefetch_related('images').all()
    brand = Brand.objects.filter()
    cat = Category.objects.all()
    print(request.method)
    brand_id = request.GET.get('brand_id')
    print(brand_id)
    if brand_id:
        print('hello')
        data = Product.objects.filter(brand_id=Brand.objects.get(brand_id=brand_id))
    if request.method == 'POST':
        search = request.POST.get('search')
        if search:
            data = Product.objects.filter(
                Q(product_name__icontains=search) | Q(description__icontains=search) | Q(price__icontains=search) | Q(
                    brand_id__brand_name__icontains=search))
            print(search)
            return render(request, 'search.html', {'products': data})
        return render(request, 'search.html', {'products': data, 'cat': cat})
    return render(request, 'search.html', {'products': data, 'cat': cat, 'brands': brand})


def brand(request):
    data = Brand.objects.all()
    cat = Category.objects.all()
    print(data.values())
    return render(request, 'brand.html', {'datas': data, 'cat': cat})


def wishlist(request):
    print("qwwwwwwwwwwwwwwwwwwwwww")
    if 'user' in request.session:
        email = request.session.get('user')
        data = Wishlist.objects.filter(user_id=User.objects.get(email=request.session['user']))
        print(data.values())
        return render(request, 'wishlist.html', {'wishlist': data})
    else:
        return redirect('/login')


def dlt_listproduct(request, list_id):
    print("rtttttttttttttttttttttttttttttt")
    data = Wishlist.objects.get(list_id=list_id)
    data.delete()
    return redirect('/wishlist')


def offers(request):
    events = Event.objects.all()
    return render(request, 'offers.html',  {'events': events})


def reviewrating(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        review = request.POST.get('review')
        print(rating, review)
        data = ReviewRating()
        data.rating = rating
        data.review = review
        data.user_id = User.objects.get(email=request.session['user'])
        data.save()
        print("Review successfully  added.............!")
        return redirect('product/{id}')
    return render(request, 'reviewrating.html')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('user_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        print(username, email, phone_number, password)
        if User.objects.filter(email=email).exists():
            return render(request, 'user-signup.html', {'error_message': 'invalid'})
        else:
            data = User(user_name=username, email=email, phone_number=phone_number, password=password)
            data.save()
            print("signup successfully .............!")
            return redirect('/login/')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        email1 = request.POST.get('email')
        password1 = request.POST.get('password')
        data = User.objects.filter(email=email1, password=password1)
        if data is not None:
            request.session['user'] = email1
            print('login successfully ..............!')
            return redirect('/')
        else:
            print('invalid')
            return render(request, 'login.html', {'error_message': 'Invalid email_id or password'})
    return render(request, 'login.html')


def profile(request):
    if 'user' in request.session:
        data1 = request.session['user']
        print(data1)
        data = User.objects.filter(email=data1)
        user_image = UserImage.objects.filter(user_id=User.objects.get(email=data1)).first()
        print(user_image)
        return render(request, 'profile.html', {'data': data, 'user_image': user_image})
    else:
        return redirect('/login')


def view_address(request):
    print('address Function called')

    if 'user' in request.session:
        # user = request.session['user ']
        data = UserAddress.objects.filter(user_id=User.objects.get(email=request.session['user']))
        return render(request, 'view_address.html', {'data': data})
    else:
        return redirect('/login')


def address(request):
    if 'user' in request.session:
        email = request.session.get('user')
        print(email)
        if request.method == "POST":
            house_id = request.POST.get('house_id')
            house_name = request.POST.get('house_name')
            house_number = request.POST.get('house_number')
            place = request.POST.get('place')
            post = request.POST.get('post')
            pin = request.POST.get('pin')
            landmark = request.POST.get('landmark')
            city = request.POST.get('city')
            print(house_id, house_id, house_name, house_number, place, post, pin, landmark, city)
            print(User.objects.filter(email=email))
            data = UserAddress()
            data.house_name = house_name
            data.house_number = house_number
            data.place = place
            data.post = post
            data.pin = pin
            data.landmark = landmark
            data.city = city
            data.user_id = User.objects.get(email=email)
            data.city_name = LocationCity.objects.get(city_name=city)
            data.save()
            print("Address successfully  added .............!")
            return redirect('profile')
        return render(request, 'address.html')
    else:
        return redirect('login')


def edit_address(request, house_id):
    data = UserAddress.objects.filter(house_id=house_id)
    if 'user' in request.session:
        email = request.session.get('user')
        if request.method == 'POST':
            house_name = request.POST.get('house_name')
            house_number = request.POST.get('house_number')
            place = request.POST.get('place')
            post = request.POST.get('post')
            pin = request.POST.get('pin')
            landmark = request.POST.get('landmark')
            city = request.POST.get('city')
            print(house_id, house_id, house_name, house_number, place, post, pin, landmark, city)
            data = UserAddress.objects.get(house_id=house_id)
            data.house_name = house_name
            data.house_number = house_number
            data.place = place
            data.post = post
            data.pin = pin
            data.landmark = landmark
            data.city = city
            data.user_id = User.objects.get(email=email)
            data.city_name = LocationCity.objects.get(city_name=city)
            data.save()
            print("Address successfully  added .............!")
            return redirect('view_address')

        return render(request, 'edit_address.html', {'data': data})
    else:
        return redirect('login')


def dlt_address(request, house_id):
    print("rtttttttttttttttttttttttttttttt")
    data = UserAddress.objects.get(house_id=house_id)
    data.delete()
    return redirect('view_address')


def logout(request):
    del request.session['user']
    return redirect('login')
