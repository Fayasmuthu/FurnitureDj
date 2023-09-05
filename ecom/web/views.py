from django.shortcuts import render,redirect

# Create your views here.

from .models import Product,Carousel,Order,Orderitem
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib import messages
# Create your views here.
# Function

def index(request):
    context={
        'prod' : Product.objects.all(),
        'caro' : Carousel.objects.all()
    }
    
    return render(request,"web/index.html",context)

def login1(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        User=authenticate(username=username,password=password)
        if User is not None:
            login(request, User)
            return redirect('index')
        else:
            messages.warning(request,'invalid details')
            return redirect('login')

    return render(request,"web/account/login.html")


def signup(request):
    if request.method=="POST":
        username=request.POST.get("user_1")
        firstname=request.POST.get("first_1")
        lastname=request.POST.get("last_1")
        email=request.POST.get("email_1")
        password=request.POST.get("password_1")
        confirm_password=request.POST.get("password_2")

        if password==confirm_password:
            customer=User.objects.create_user(username,email,password)
            customer.first_name=firstname
            customer.last_name=lastname
            customer.save()
            return redirect('login')
    return render(request, "web/account/signup.html")

def logout1(request):
    logout(request)
    return render(request,"web/account/login.html")


# copy django shopping cart




@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")

@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")


@login_required(login_url="login")
def cart_detail(request):
    return render(request, 'web/cart/cart.html')

@login_required(login_url="login")
def checkout(request):
    return render(request, 'web/cart/checkout.html')

@login_required(login_url="login")
def placeorder(request):


    if request.method=="POST":
        uid=request.session.get('_auth_user_id')
        user=User.objects.get(id=uid)
        
        Cart=request.session.get('cart')
        First_Name=request.POST.get('Fname')
        Last_Name=request.POST.get('Lname')
        Country=request.POST.get('Country')
        Address=request.POST.get('Saddress')
        City=request.POST.get('City')
        State=request.POST.get('State')
        Pincode=request.POST.get('Pin')
        Phone=request.POST.get('Phone')
        Email=request.POST.get('Email')


        order_1=Order(
            user=user,
            First_Name=First_Name,
            Last_Name=Last_Name,
            Country=Country,
            Address=Address,
            City=City,
            State=State,
            Pincode=Pincode,
            Phone=Phone,
            Email=Email,

            

        )
        order_1.save()

        for i in Cart:
            a=float(Cart[i]['price'])
            b=int(Cart[i]['quantity'])
            total=a*b

            order_1=Orderitem(
                Order=order_1,
                Product=Cart[i]['name'],
                image=Cart[i]['image'],
                price=Cart[i]['price'],
                qunatity=Cart[i]['quantity'],
                total=total
            )

            order_1.save()

    return render(request, 'web/cart/placeorder.html')

@login_required(login_url="login")
def confirm1(request):
    
    return render(request, 'web/cart/confirm.html')
