from django.shortcuts import render, redirect
from main.models import Product, Slider, About_section, Coustomer, Brand
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Create your views here.
def index(request):

    products = Product.objects.all()[:9]
    sliders = Slider.objects.all()
    abouts = About_section.objects.all()
    comments = Coustomer.objects.all()

    context = {
        'products': products,
        'sliders': sliders,
        'abouts': abouts,
        'comments': comments,
    }
    return render(request, 'index.html', context)
    

def login_page(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request, 'login.html')
    return render(request, 'login.html')


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        conform_password = request.POST['confirm_password']

        if password == conform_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already taken.')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password are not matching..')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def product(request):

    products = Product.objects.all()
    brands = Brand.objects.all()

    context = {
        'products': products,
        'brands': brands,
    }
    return render(request, 'product.html', context)

def search(request):
    query = request.GET['query']
    brands = Brand.objects.all()

    products = Product.objects.filter(Q(name__icontains=query) |
    Q(price__icontains=query) | Q(brand__name__icontains=query))

    context = {
        'products': products,
        'query': query,
        'brands': brands,
    }
    return render(request, 'search.html', context)

def cart(request):
    return render(request, 'cart.html')


#add to cart functions
@login_required(login_url="/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")


@login_required(login_url="/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required(login_url="/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")


@login_required(login_url="/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")


@login_required(login_url="/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')