from django.shortcuts import redirect


def login_required(func):
    def wrapper(request,id=None,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return func(request,id,*args,**kwargs)
    return wrapper


def admin_permission_required(func):
    def wrapper(request,id=None,*args,**kwargs):
        if not request.user.is_superuser:
            return redirect("signin")
        else:
            return func(request,id,*args,**kwargs)
    return wrapper
