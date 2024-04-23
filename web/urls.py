from django.contrib import admin
from django.urls import path,include
from .import views
from .views import CreateStripeCheckoutSessionView
urlpatterns = [
   path("",views.index,name="index"),
   path("singup",views.singup,name="singup"),
   path("login",views.login1,name="login1"),
   path("logout",views.logout1,name="logout"),
   path("price",views.price,name="price"),
   path("success",views.success,name="success"),
   path("error",views.error,name="error"),

   path(
        "create-checkout-session/",
        CreateStripeCheckoutSessionView.as_view(),
        name="create-checkout-session"
    ),
   



]
