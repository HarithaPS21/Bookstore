from django.shortcuts import render,redirect
from customer import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from owner.models import Book
from owner.models import Order
from customer.filters import BookFilter
from customer.decorators import login_required

# Create your views here.

# registration,login,logout
# auth application ...........builtin application for authentication
# AbstractBaseUser -> AbstractUser -> User ......child

def signup_view(request):
    form=forms.UserRegistrationForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            return render(request,"customer/signup.html",{"form":form})
    return render(request,"customer/signup.html",context)


def signin_view(request):
    form=forms.LoginForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['user_name']
            password=form.cleaned_data['password']
            user=authenticate(request,username=user_name,password=password)
            if user:
                login(request,user)
                return redirect("home")
            else:
                messages.error(request,"invalid credentials")
                return redirect("signin")
        else:
            return render(request,"customer/login.html",{"form":form})
    return render(request,"customer/login.html",context)


@login_required
def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")


@login_required
def user_home(request,*args,**kwargs):
    books=Book.objects.all()
    context={"books":books}
    return render(request,"customer/user_home.html",context)


@login_required
def order_create(request,id,*args,**kwargs):

    book=Book.objects.get(id=id)
    form=forms.OrderForm(initial={"product":book})
    context={"form":form,"book":book}
    if request.method=="POST":
        form=forms.OrderForm(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            order.user=request.user
            order.save()
            book.copies-=1
            book.save()
            messages.success(request,"order has been placed")
            return redirect("home")
        else:
            return render(request, "customer/order_create.html", {"form":form})
    return render(request,"customer/order_create.html",context)


@login_required
def orders_list(request,*args,**kwargs):

    orders=Order.objects.filter(user=request.user).exclude(status="cancelled")
    context={"orders":orders}
    return render(request,"customer/orders_list.html",context)

@login_required
def cancel_order(request,id,*args,**kwargs):
    order=Order.objects.get(id=id)
    order.status="cancelled"
    order.save()
    return redirect("home")

@login_required
def book_find(request):
    filters=BookFilter(request.GET,queryset=Book.objects.all())
    return render(request,"customer/bookfilter.html",{"filter":filters})