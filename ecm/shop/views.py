from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect


from .models import Category,Products
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
def index(request):
    return HttpResponse("Hello")


def allProdCat(request,c_slug=None):
    c_page = None
    products_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category,slug=c_slug)
        products_list = Products.objects.all().filter(category=c_page,available=True)
    else:
        products_list = Products.objects.all().filter(available=True)
    paginator=Paginator(products_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)



    return render(request,'category.html',{'category':c_page,'products':products})

def proDetail(request,c_slug,product_slug):
    try:
        product=Products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm=request.POST['confirm']
        if password==confirm:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken..!")
                return render(request,'rederror.html')
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request,"You Used an Existing Mail!")
            #     return redirect("register")
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return render(request,"login.html")
                print("User Registered")
        else:
            messages.info(request,"Passwords not matching..!")
            return render(request,'rederror.html')
        return redirect('/')
    return render(request,"register.html")

# --> login

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"redin.html")
        else:
            messages.info(request,"User Not Found!!!")
            return render(request,"logerror.html")
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def redin(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if password == password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken..!")
                return render(request,"message.html")
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request,"You Used an Existing Mail!")
            #     return redirect("register")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return render(request, "message.html")
                print("User Registered")
        else:
            messages.info(request, "Passwords not matching..!")
            return render(request, "sub_form.html")
        return render(request, "message.html")
    return render(request, "sub_form.html")
# def subf(request):
#     return render(request,'message.html')
def success(request):
    return render(request,'message.html')

