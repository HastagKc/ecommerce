from django.shortcuts import redirect, render
from .models import *
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


# Create your views here.


def index(request):
    # category
    cate = Category.objects.all()
    cateid = request.GET.get('category')
    print(cateid)

    if cateid:
        product = Product.objects.filter(sub_category=cateid)
    else:
        product = Product.objects.all()

    # paginator
    paginator = Paginator(product, 4)
    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)
    total = data.paginator.num_pages

    # context
    context = {
        'product': product,
        'cate': cate,
        'data': data,
        'total': total,
        'num': [i+1 for i in range(total)],

    }
    return render(request, 'main/index.html', context=context)


def cart(request):
    return render(request, 'main/cart.html')


def checkout(request):
    return render(request, 'main/checkout.html')


def contact(request):
    return render(request, 'main/contact-us.html')


def product_details(request):
    return render(request, 'main/product-details.html')


def shop(request):
    return render(request, 'main/shop.html')


def blog(request):
    return render(request, 'main/blog.html')


def blog_single(request):
    return render(request, 'main/blog-single.html')


def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('register')
    return render(request, 'auth/login.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['fullname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conform_password = request.POST['confirm_password']

        try:
            validate_password(password)
            if password == conform_password:
                if User.objects.filter(username=name).exists():
                    messages.error(request, 'Username already exists')
                    return render(request, 'auth/register.html', {
                        'full_name': name,
                        'username': username,
                        'email': email,
                    })
                elif User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return render(request, 'auth/register.html', {
                        'full_name': name,
                        'username': username,
                        'email': email,
                    })
                else:
                    user = User.objects.create_user(
                        first_name=name,
                        username=username,
                        email=email,
                        password=password
                    )
                    user.save()
                    messages.success(request, "Registered Successfully")
                    return redirect('log_in')
            else:
                messages.error(request, "Passwords do not match")
                return render(request, 'auth/register.html', {
                    'full_name': name,
                    'username': username,
                    'email': email,
                })

        except ValidationError as e:
            for error in e.messages:
                messages.error(request, error)
                return redirect('register')

    return render(request, 'auth/register.html')
