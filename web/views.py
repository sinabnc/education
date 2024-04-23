from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.contrib import messages
from .  models import contact
from django.conf import settings
import stripe
from django.views import View


# Create your views here.

def index(request):

    if request.method=='POST':
      name=request.POST.get("name")
      email=request.POST.get("email")
      phone=request.POST.get("phone")

      contact1=contact(
         name=name,
         email=email,
         phone=phone
      )
      contact1.save()
    return render(request,"web/index.html")


def login1(request):
    user = request.user
    if user.is_authenticated:
       return redirect('index')
    elif request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get('pass')
        user = authenticate(request, username=username,password =password  )
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
             messages.warning(request,'invalid details')
             return redirect("login1")
             
        
       


    return render(request,'web/login.html')


def singup(request):
    if request.method=="POST":
      username=request.POST.get("username")
      firstname=request.POST.get("lname")
      pass1=request.POST.get('pass')
      email=request.POST.get('email')

      if User.objects.filter(username=username).exists():
        messages.warning(request,'User already exist')
        return redirect('singup')
      
      else:
        user = User.objects.create_user(username,email, pass1)
        user.first_name=firstname
        user.save()
        return redirect('login1')
    return render(request,'web/singup.html')

@login_required(login_url="login1")
def price(request):
   return render(request,"web/price.html")


def logout1(request):
   logout(request)
   return redirect('index')



stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateStripeCheckoutSessionView(View):
    """
    Create a checkout session and redirect the user to Stripe's checkout page
    """

    def post(self, request, *args, **kwargs):
        

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": int(69)*100,
                        "product_data": {
                            "name": 'Subscription',
                          
                           
                        },
                    },
                    "quantity": 1,
                }
            ],
          
            mode="payment",
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
        )
        return redirect(checkout_session.url)
   

def success(request):
   return render(request,"web/success.html")


def error(request):
   return render(request,"web/error.html")