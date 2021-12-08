from django.shortcuts import render, redirect

from owner import forms

from owner.models import Book,Order

from django.contrib import messages

from django.db.models import Count

from customer.decorators import admin_permission_required


# Create your views here.
# 8000/owner/books/
# 8000/owner/books/add
# 8000/owner/books/list
# 8000/owner/books/change/id
# 8000/owner/books/remove/id


def home(request):
    return render(request, "index.html")


def signupview(request):
    form=forms.RegistrationForm()
    context={}
    context['form']=form
    if request.method == "POST":
        form=forms.RegistrationForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            user_name=form.cleaned_data['user_name']
            email=form.cleaned_data['email']
            password1=form.cleaned_data['password1']
            password2=form.cleaned_data['password2']
            context={}
            context['first_name']=first_name
            context['username']=user_name
            context['email']=email
            context['password1']=password1
            context['password2']=password2
            return redirect("signin")
    return render(request,"register.html",context)


def signinview(request):
    form=forms.LoginForm()
    context={}
    context['form']=form
    if request.method=="POST":
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['user_name']
            password=form.cleaned_data['password']
            context={}
            context['user_name']=user_name
            context['password']=password
            return redirect("addbook")
    return render(request,"signin.html",context)


@admin_permission_required
def book_create(request,*args,**kwargs):
   form = forms.BookForm()
   context = {'form' : form}
   if request.method == 'POST':
       form = forms.BookForm(request.POST,request.FILES)
       if form.is_valid():
           # book_name=form.cleaned_data['book_name']
           # author=form.cleaned_data['author']
           # price=form.cleaned_data['price']
           # copies=form.cleaned_data['copies']
           # # print(book_name,author,price,copies)
           # # context={}
           # # context['book_name']=book_name
           # # context['author']=author
           # # context['price']=price
           # # context['copies']=copies
           # book=Book(book_name=book_name,author=author,price=price,copies=copies)
           # book.save()
           form.save()
           messages.success(request,"book added successfully")
           return redirect("listbook")
       else:
           return render(request, "book_add.html", {"form":form})
   return render(request,"book_add.html",context)


@admin_permission_required
def book_list(request,*args,**kwargs):
    form=forms.BookSearchForm()
    books=Book.objects.all()
    context={}
    context['books']=books
    context['form']=form
    if request.method=="POST":
        form=forms.BookSearchForm(request.POST)
        if form.is_valid():
            book_name=form.cleaned_data['book_name']
            books = Book.objects.filter(book_name__contains=book_name)
            context['books'] = books
            return render(request, "list_book.html", context)

    return render(request,"list_book.html",context)
    # form=forms.BookForm()
    # context={"form" : form}
    # if request.method == 'POST':
    #     form=forms.BookForm(request.POST)
    #     if form.is_valid():
    #         book_name=form.cleaned_data['book_name']
    #         author=form.cleaned_data['author']
    #         price=form.cleaned_data['price']
    #         copies=form.cleaned_data['copies']
    #         # print(form.cleaned_data)
    #         context={}
    #         context['book_name']=book_name
    #         context['author']=author
    #         context['price']=price
    #         context['copies']=copies
    #         return render(request,"list_book.html",context)
    # return render(request,"list_book.html",context)


@admin_permission_required
def book_update(request,id,*args,**kwargs):
    book = Book.objects.get(id=id)
    # data = {
    #     'book_name': book.book_name,
    #     'author': book.author,
    #     'price': book.price,
    #     'copies': book.copies
    # }
    form = forms.BookEditForm(instance=book)
    context = {}
    context['form'] = form
    if request.method=="POST":
       form=forms.BookEditForm(request.POST,instance=book,files=request.FILES)
       if form.is_valid():
           # book_name = form.cleaned_data['book_name']
           # author = form.cleaned_data['author']
           # price = form.cleaned_data['price']
           # copies = form.cleaned_data['copies']
           # book.book_name=book_name
           # book.author=author
           # book.price=price
           # book.copies=copies
           # book.save()
           form.save()
           return redirect("listbook")
       else:
           return render(request,"change_book.html",{"form":form})
    return render(request,"change_book.html",context)


@admin_permission_required
def book_remove(request,id,*args,**kwargs):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect("listbook")


@admin_permission_required
def book_detail(request,id,*args,**kwargs):
    book=Book.objects.get(id=id)
    context={}
    context['book']=book
    return render(request,"book_detail.html",context)


@admin_permission_required
def dashboard(request,*args,**kwargs):
    stocks=Book.objects.all().order_by("copies")
    # stocks=Book.objects.values("book_name").annotate(count=Count("book_name"))
    reports=Order.objects.values("product__book_name").annotate(counts=Count("product"))
    orders=Order.objects.filter(status="ordered")
    context={"orders":orders,"reports":reports,"stocks":stocks}
    return render(request,"dashboard.html",context)


@admin_permission_required
def dash_edit(request,id,*args,**kwargs):
    order=Order.objects.get(id=id)
    form = forms.DashEditForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.DashEditForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    return render(request,"dashedit.html",context)
