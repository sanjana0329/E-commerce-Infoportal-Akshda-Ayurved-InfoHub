from django.shortcuts import (
    redirect,
)
from functools import wraps

def is_admin(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.type == "ADMIN" or request.user.is_superuser:
            return view_func(request, *args, **kwargs)    
        else:
            return redirect("/")
    return wrap

def is_manager(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.type == "SHIPPER" or request.user.is_superuser:
            return view_func(request, *args, **kwargs)    
        else:
            return redirect("/")
            
    return wrap

def is_agent(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.type == "CARRIER" or request.user.is_superuser:
            return view_func(request, *args, **kwargs)    
        else:
            return redirect("/")
            
    return wrap


def Admin_has_permissions(view_func):
    @wraps(view_func)
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login')
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return redirect("/")
    return wrap

def Shipper_has_permissions(view_func):
    @wraps(view_func)
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login')
        allowed_types = ["SHIPPER"]
        if request.user.is_superuser or getattr(request.user, 'type', None) in allowed_types:
            return view_func(request, *args, **kwargs)
        else:
            return redirect("/")
    return wrap

def Carrier_has_permissions(view_func):
    @wraps(view_func)
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login')
        allowed_types = ["CARRIER"]
        if request.user.is_superuser or getattr(request.user, 'type', None) in allowed_types:
            return view_func(request, *args, **kwargs)
        else:
            return redirect("/")
    return wrap

def has_permissions_mixin(view_func):
    @wraps(view_func)
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login')
        allowed_types = ["CARRIER", "SHIPPER"]
        if request.user.is_superuser or getattr(request.user, 'type', None) in allowed_types:
            return view_func(request, *args, **kwargs)
        else:
            return redirect("/")
    return wrap