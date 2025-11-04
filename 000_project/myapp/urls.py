

from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",index,name="index"),
    path("accounts",accounts,name="accounts"),
    path("cart",cart,name="cart"),
    path("checkout",checkout,name="checkout"),
    path("compare",compare,name="compare"),
    path("details",details,name="details"),
    path("login-register",login_register,name="login-register"),
    path("shop",shop,name="shop"),
    path("wishlist",wishlist,name="wishlist"),
    path("allcategories",allcategories,name="allcategories"),
    path("allproducts",allproducts,name="allproducts"),

    path("register",register,name="register"),
    path("login",user_login,name="login"),
    path("user-logout",user_logout,name="user-logout"),

    path('addtocart',add_to_cart,name="addtocart"),
    path('deletecart',deletecart,name='deletecart'),
    path('changeqty',changeqty,name='changeqty'),

    path('payment',payment,name='payment'),
    path("addaddress",addaddress,name="addaddress")

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)