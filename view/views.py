from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login as alogin, logout as alogout, authenticate
from django.contrib.auth.models import User
from product.models import Prod, Special
from cart.models import CartItem
from book.models import Order
import datetime

def home(request):
    s=Special.objects.all()
    p=Prod.objects.all()
    return render(request, 'index.html', {'p':p, 's':s})

def product(request):
    s=Special.objects.all()
    p=Prod.objects.all()
    return render(request, 'products.html', {'p':p, 's':s})

def view_product(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        p= Prod.objects.get(pk=id)
        return render(request, 'view_product.html', {'p':p})    
    else:

        return HttpResponse("404 error")

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')    

def handle_login(request):
    if request.method == 'POST':
        uname = request.POST.get("uname")
        pass1 = request.POST.get("pass")
        user = authenticate(username=uname, password=pass1)
        if user is not None:
            alogin(request, user)

            # messages.success(request, "Logged in")
            return redirect('home')
        else:
            # messages.info(request,'invalid credentials')
            return redirect('loginx')  
    return redirect('home') 

def logout(request):
    alogout(request)
    return redirect('home')                   

def handle_signup(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        uname = request.POST.get("uname")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        if pass1==pass2:
            


            myuser = User.objects.create_user(username=uname, email=email, password=pass1,)
            myuser.first_name = name
            myuser.save()
            # messages.success(request, "Your account has been created")
            print('success')
            return redirect("home")
    else:

        return HttpResponse("404 error") 
    
def order_now(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            prod_id1 = request.POST.get("id")
            p= Prod.objects.get(pk=prod_id1)
            
            
            
            now = datetime.datetime.now()
            date_string = now.strftime("%Y%m%d%H%M%S")
            date1 = int(date_string)
            o= Order(prod_id=p.pk, quantity=1, user_id=request.user.pk, order_main_id=date1, status='Ordered')
            
           
            # c= Cartitem(prod_id=p.pk, quantity=1, user_id=request.user.pk)
            # c.save()
            o.save()
            
            return redirect('home')   
        else:
            return HttpResopnce('404 error')
    else:

        return HttpResponse("Login To Order")   
    
def my_orders(request):
    if request.user.is_authenticated:
        o=Order.objects.filter(user_id=request.user.pk)
        return render(request, 'my_orders.html', {'o':o})
    else:
        return HttpResponse("Login To Check")  
    
def add_cart(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id = request.POST.get("id")
            p= Prod.objects.get(pk=id)
            c= CartItem(prod_id=p.pk, quantity=1, user_id=request.user.pk)
            c.save()
            print(p)
            return redirect('home')   
        else:
            return HttpResopnce('404 error')    
    else:

        return HttpResponse("Login TO Add Cart")   

def mycart(request):
    if request.user.is_authenticated:
        c= CartItem.objects.filter(user_id=request.user.pk)
        t=0
        for item in c:
            t=t+item.quantity*item.prod.price
        return render(request, 'cart.html', {'c':c, 't':t})
    else:

        return HttpResponse("Login TO Buy")  

def handle_cart(request):
    if request.method == 'POST':
        
        c= CartItem.objects.filter(user_id=request.user.pk)
        
        now = datetime.datetime.now()
        date_string = now.strftime("%Y%m%d%H%M%S")
        date_int = int(date_string)
        
        for item in c:
            print(item.prod)
            o=Order(prod_id=item.prod_id, quantity=item.quantity, user_id=request.user.pk, order_main_id=date_int)
            o.save()
        # c= Cartitem(prod_id=p.pk, quantity=1, user_id=request.user.pk)
        # c.save()
        
        return redirect('home')    
    else:

        return HttpResponse("Login To Order")    

def edit_cart_item(request):
    if request.user.is_authenticated:    
        if request.method=='POST':
            id= request.POST.get('id')
            
            c= CartItem.objects.get(pk=id)
            
            return render(request, 'edit_cart.html', {'c':c})
        else:
            return HttpResponse('404 ERROR')
    else:
        return HttpResponse('Please Login')    

def handle_edit_cart_item(request):
    if request.user.is_authenticated:    
        if request.method=='POST':
            id= request.POST.get('id')
            q= request.POST.get('q')
            print('q')
            c= CartItem.objects.get(pk=id)
            c.quantity=q
            c.save()
            return redirect('cart')
        else:
            return HttpResponse('404 ERROR')
    else:
        return HttpResponse('Please Login')

def delete_cart_item(request):
    if request.user.is_authenticated:    
        if request.method=='POST':
            id= request.POST.get('id')
            c= CartItem.objects.get(pk=id)
            c.delete()
            return redirect('cart')
        else:
            return HttpResponse('404 ERROR')
    else:
        return HttpResponse('Please Login')  

def checkout(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        p= Prod.objects.get(pk=id)
        c= Cartitem.objects.filter(user_id=request.user.pk)
        t=p.prod_price
        for item in c:
            t=t+item.quantity*item.prod.prod_price
        print(p)
        return render(request, 'checkout.html', {'p':p, 'c':c, 't':t})    
    else:

        return HttpResponse("Login TO Buy")         

def handle_checkout(request):
    if request.method == 'POST':
        prod_id1 = request.POST.get("prod_id")
        p= Prod.objects.get(pk=prod_id1)
        print(p)
        c= Cartitem.objects.filter(user_id=request.user.pk)
        
        now = datetime.datetime.now()
        date_string = now.strftime("%Y%m%d%H%M%S")
        date_int = int(date_string)
        o1= Order(prod_id=p.pk, quantity=1, user_id=request.user.pk, order_main_id=date_int)
        
        for item in c:
            print(item.prod)
            o=Order(prod_id=item.prod_id, quantity=item.quantity, user_id=request.user.pk, order_main_id=date_int)
            o.save()
        # c= Cartitem(prod_id=p.pk, quantity=1, user_id=request.user.pk)
        # c.save()
        o1.save()
        print(p)
        return redirect('home')    
    else:

        return HttpResponse("Login To Order")       
    
def order_now_cart(request):
    if request.method == 'POST':
        prod_id1 = request.POST.get("id")
        p= CartItem.objects.get(pk=prod_id1)
        
        
        
        now = datetime.datetime.now()
        date_string = now.strftime("%Y%m%d%H%M%S")
        date1 = int(date_string)
        o= Order(prod_id=p.pk, quantity=p.quantity, user_id=request.user.pk, order_main_id=date1, status='Ordered')
        
       
        # c= Cartitem(prod_id=p.pk, quantity=1, user_id=request.user.pk)
        # c.save()
        o.save()
        
        return redirect('home')    
    else:

        return HttpResponse("Login To Order")      
