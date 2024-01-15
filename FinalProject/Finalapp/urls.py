from django.urls import path
from Finalapp import views

urlpatterns = [
    path('indexpage/', views.indexpage, name="indexpage"),
    path('categoryaddpage/', views.categoryaddpage, name="categoryaddpage"),
    path('categorydata/', views.categorydata, name="categorydata"),
    path('categorydisplay/', views.categorydisplay, name="categorydisplay"),
    path('categoryedit/<int:Categoryid>/', views.categoryedit, name="categoryedit"),
    path('categoryupdate/<int:Categoryid>/', views.categoryupdate, name="categoryupdate"),
    path('deletecategory/<int:Categoryid>/', views.deletecategory, name="deletecategory"),
    path('productadd/', views.productadd, name="productadd"),
    path('productdata/', views.productdata, name="productdata"),
    path('productdisplay/', views.productdisplay, name="productdisplay"),
    path('productedit/<int:Productid>/', views.productedit, name="productedit"),
    path('productupdate/<int:Productid>/', views.productupdate, name="productupdate"),
    path('deleteproduct/<int:Productid>/', views.deleteproduct, name="deleteproduct"),
    path('adminloginpage/', views.adminloginpage, name="adminloginpage"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('displaycontact/', views.displaycontact, name="displaycontact"),
    path('deletecontact/<int:Contactid>/', views.deletecontact, name="deletecontact"),
    path('displaybooking/', views.displaybooking, name="displaybooking"),
    path('deletereservation/<int:Tableid>/', views.deletereservation, name="deletereservation"),
    path('displaysignup/', views.displaysignup, name="displaysignup"),
    path('deletesignup/<int:Loginid>/', views.deletesignup, name="deletesignup"),
]