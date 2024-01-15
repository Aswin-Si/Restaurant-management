from django.urls import path
from Frontend import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('menupage/', views.menupage, name="menupage"),
    path('reservationpage/', views.reservationpage, name="reservationpage"),
    path('reservationdata/', views.reservationdata, name="reservationdata"),
    path('Gallerypage/', views.Gallerypage, name="Gallerypage"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('contactdetails/', views.contactdetails, name="contactdetails"),
    path('menufilteredpage/<cat_name>/', views.menufilteredpage, name="menufilteredpage"),
    path('singleproduct/<int:productid>/', views.singleproduct, name="singleproduct"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('signupdata/', views.signupdata, name="signupdata"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('cartpage/', views.cartpage, name="cartpage"),
    path('cartdetails/', views.cartdetails, name="cartdetails"),
    path('deletecartdetail/<int:cartid>/', views.deletecartdetail, name="deletecartdetail"),
    path('orderpage/', views.orderpage, name="orderpage"),
    path('checkoutdata/', views.checkoutdata, name="checkoutdata"),
]