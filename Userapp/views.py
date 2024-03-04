from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.template import loader
from Sellerapp.models import *
from Userapp.models import *
from Adminapp.models import *
from Userapp.models import UserAddress, UserCart
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
    users = 'no user'
    if 'user' in request.session:
        current_user = request.session['user']
        users = User.objects.get(email=current_user)

    return render(request, 'homepage.html',{'products': data, 'user': users, 'cat': cat, 'categorized_products': categorized_products})


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
            cart_data = UserCart()
            cart_data.product_id = Product.objects.get(product_id=id)
            cart_data.quantity = quantity
            cart_data.user_id = User.objects.get(email=email)
            cart_data.save()
            return redirect('/cart')
    return render(request, 'single-product.html', {'products': data, 'review': data})


def cart(request):
    print("sdfghj")
    # product = Product.objects.filter(product_id=request.POST.get('product_id'))
    if 'user' in request.session:
        # cart_items = UserCart.objects.filter(user_id=User.objects.get(email=request.session.get('user')))
        # total_price = cart_items.aggregate(total_price=Sum('product_id__price' * 'quantity'))
        #
        # # If there are no items in the cart, total_price will be None, so handle it accordingly
        # total_price = total_price['total_price'] if total_price['total_price'] is not None else 0
        # print(f' total: {total_price}')
        if request.method == 'POST':

            qty = int(request.POST['quantity'])

            product_id = int(request.POST["product_id"])
            cart_obj = UserCart()
            cart_obj.product_id = Product.objects.get(product_id=product_id)
            cart_obj.quantity = qty
            cart_obj.user_id = User.objects.get(email=request.session.get('user'))
            cart_obj.save()

        email = request.session.get('user')
        data = UserCart.objects.filter(user_id=User.objects.get(email=email))
        print(data.values())
        return render(request, 'cart.html', {'cart': data})
    else:
        return redirect('/login')

def buy(request):
    if 'user' in request.session:
        email = request.session.get('user')
        print("aaaaaaaaaaaaaaaaaaaaaa")
        product_details=Order.objects.filter(user_id=User.objects.get(user_id=request.session('user')))
        total_price = UserCart.objects.filter(user_id=User.objects.get(email=request.session.get('user'))).aggregate(
            total_price=Sum(F('product_id__price') * F('quantity'), output_field=models.DecimalField())
            )['total_price'] or Decimal('0.00')
        print(f"Total price for user : ₹{total_price}")
        address = UserAddress.objects.all()

        # data = Cart.objects.filter(user_id=User.objects.get(email=email))
        # print(data.values())

        # amount = 0
        # for x in cart:
        #     value = x.quantity * x.product_id.price
        #     amount = amount + value
        #     total_price = amount + 50

        return render(request, 'buynow.html', {'cart': product_details,'total_price': total_price,'address': address})
    else:
        return redirect('/login')

def checkout(request):
    if 'user' in request.session:
        email = request.session.get('user')
        data = UserAddress.objects.filter(user_id=User.objects.get(email=email))
        return render(request, 'checkout.html', {'cart': data})


def dlt_product(request, cart_id):
    print("rtttttttttttttttttttttttttttttt")
    data = UserCart.objects.get(cart_id=cart_id)
    data.delete()
    return redirect('/cart')


def category(request, main_category_id):
    print(main_category_id)
    print("category function")
    data = Category.objects.get(main_category_id=main_category_id)
    data1 = Product.objects.select_related('seller_id').prefetch_related('images').all()
    print(data)
    data1 = Product.objects.filter(main_category_id=data)
    cat = Category.objects.all()
    print(data1.values())
    if request.method == 'POST':
        search = request.POST.get('search')
        if 'selected_price' in request.POST:
            print(int(request.POST['selected_price']))
            data1 = data1.filter(price__lt=int(request.POST['selected_price']))
        if 'selected_discount' in request.POST:
            print(int(request.POST['selected_discount']))
            data1 = data1.filter(offer__discount__lt=int(request.POST['selected_discount']))
        data1 = data1.prefetch_related('images')
        print(data1.values())
    return render(request, 'category.html', {'category': data1, 'cat': cat, 'products': data, })


def search(request):
    print("rrrrrrrrr")
    data = Product.objects.select_related('seller_id').prefetch_related('images').all()

    offer = Offer.objects.all()
    cat = Category.objects.all()
    print(request.method)
    brand_id = request.GET.get('brand_id')
    print(brand_id)
    # offer_id = request.GET.get('offer_id')
    # print(offer_id)
    search = ''
    if brand_id:
        print('hello')

        data = Product.objects.filter(brand_id=Brand.objects.get(brand_id=brand_id))
        # data1 = Product.objects.filter(offer_id=Offer.objects.get(offer_id=offer_id))
    if request.method == 'POST':
        search = request.POST.get('search')
        if request.POST.get('search'):
            data = data.filter(Q(product_name__icontains=search) | Q(description__icontains=search) | Q(price__icontains=search) | Q(main_category_id__main_category_name__icontains=search) | Q(brand_id__brand_name__icontains=search))
            # data1 = data1.filter(Q(offer_id__offer_name__icontains=search) | Q(offer_id__discount__icontains=search))
            # print(data1.values())
        if 'selected_price' in request.POST:
            print(int(request.POST['selected_price']))
            data = data.filter(price__lt=int(request.POST['selected_price']))
        if 'selected_discount' in request.POST:
            print(int(request.POST['selected_discount']))
            data = data.filter(offer__discount__lt=int(request.POST['selected_discount']))
            data = data.prefetch_related('images')
            print(data.values())

    return render(request, 'search.html', {'products': data, 'cat': cat, 'search':search, 'brands': brand})


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
    cat = Category.objects.all()
    return render(request, 'offers.html', {'events': events, 'cat': cat})


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
            return render(request, 'signup.html', {'error_message': 'invalid'})
        else:
            data = User(user_name=username, email=email, phone_number=phone_number, password=password)
            data.save()
            print("signup successfully .............!")
            return redirect('/login')
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


def buy(request, house_id=None):
    print("xxxxxxxxxxx")
    if 'user' in request.session:
        email = request.session.get('user')
        if request.method == 'POST':
            address = UserAddress.objects.filter(house_id=house_id)
            print(address.values())
        return render(request, 'buynow.html')
    else:
        return redirect('/login')


def logout(request):
    del request.session['user']
    return redirect('/login')
