from django.shortcuts import render,redirect
from Finalapp.models import CategoryDb,ProductDb,ContactDb
from Frontend.models import ReservationDb,SignupDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages

# Create your views here.
def indexpage(request):
    return render(request, "index.html")
def categoryaddpage(request):
    return render(request, "AddCategory.html")
def categorydata(request):
    if request.method == "POST":
        cn = request.POST.get('cname')
        ci = request.FILES['cimage']
        obj = CategoryDb(CategoryName=cn, CategoryImage=ci)
        obj.save()
        messages.success(request, "Category added Successfully..!")
        return redirect (categoryaddpage)
def categorydisplay(request):
    cat = CategoryDb.objects.all()
    return render(request, "DisplayCategory.html", {'cat':cat})
def categoryedit(request,Categoryid):
    cat = CategoryDb.objects.get(id=Categoryid)
    return render(request, "EditCategory.html", {'cat':cat})
def categoryupdate(request,Categoryid):
    if request.method == "POST":
        cn = request.POST.get('c_name')
        try:
            img = request.FILES['c_image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = CategoryDb.objects.get(id=Categoryid).CategoryImage
        CategoryDb.objects.filter(id=Categoryid).update(CategoryName=cn, CategoryImage=file)
        messages.success(request, "Category updated Successfully..!")
        return redirect(categorydisplay)
def deletecategory(request, Categoryid):
    cat = CategoryDb.objects.filter(id=Categoryid)
    cat.delete()
    messages.error(request, "Product Deleted Successfully...!")
    return redirect(categorydisplay)
def productadd(request):
    cat = CategoryDb.objects.all()
    return render(request, "AddProduct.html", {'cat':cat})
def productdata(request):
    if request.method == "POST":
        ca = request.POST.get('c_name')
        pn = request.POST.get('pname')
        pp = request.POST.get('pprice')
        de = request.POST.get('pdesc')
        pi = request.FILES['pimage']
        obj = ProductDb(Category_Name=ca, ProductName=pn, ProductPrice=pp, Description=de, ProductImage=pi)
        obj.save()
        messages.success(request, "Product added Successfully..!")
        return redirect(productadd)
def productdisplay(request):
    product = ProductDb.objects.all()
    return render(request, "DisplayProduct.html", {'product':product})
def productedit(request, Productid):
    product = ProductDb.objects.get(id=Productid)
    cat = CategoryDb.objects.all()
    return render(request, "EditProduct.html", {'product':product,'cat':cat})
def productupdate(request, Productid):
    if request.method == "POST":
        cna = request.POST.get('cname')
        pna = request.POST.get('p_name')
        ppr = request.POST.get('p_price')
        pde = request.POST.get('p_desc')
        try:
            pimg = request.FILES['p_image']
            fs = FileSystemStorage()
            file = fs.save(pimg.name, pimg)
        except MultiValueDictKeyError:
            file = ProductDb.objects.get(id=Productid).ProductImage
        ProductDb.objects.filter(id=Productid).update(Category_Name=cna, ProductName=pna, ProductPrice=ppr, Description=pde, ProductImage=file)
        messages.success(request, "Product Updated Successfully..!")
        return redirect(productdisplay)

def deleteproduct(request, Productid):
    product = ProductDb.objects.get(id=Productid)
    product.delete()
    messages.error(request, "Product Deleted Successfully...!")
    return redirect(productdisplay)

def adminloginpage(request):
    return render(request, "AdminPage.html")
def adminlogin(request):
    if request.method == "POST":
        un = request.POST.get('uname')
        pwd = request.POST.get('upassword')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un, password=pwd)
            if user is not None:
                login(request, user)
                request.session['username']=un
                request.session['password']=pwd
                messages.success(request, "Login Successfully..!")
                return redirect(indexpage)
            else:
                messages.error(request, "Invalid Username Or Password")
                return redirect(adminloginpage)
        else:
            messages.error(request, "Invalid Username Or Password")
            return redirect(adminloginpage)
def adminlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout Successfully..!")
    return redirect(adminloginpage)

def displaycontact(request):
    contact = ContactDb.objects.all()
    return render(request, "ContactDisplay.html", {'contact':contact})
def deletecontact(request, Contactid):
    query = ContactDb.objects.get(id=Contactid)
    query.delete()
    return redirect(displaycontact)

def displaybooking(request):
    reservation = ReservationDb.objects.all()
    return render(request, "BookingDisplay.html", {'reservation':reservation})
def deletereservation(request, Tableid):
    table = ReservationDb.objects.get(id=Tableid)
    table.delete()
    return redirect(displaybooking)
def displaysignup(request):
    signup = SignupDb.objects.all()
    return render(request, "Signupdisplay.html", {'signup':signup})
def deletesignup(request, Loginid):
    users = SignupDb.objects.get(id=Loginid)
    users.delete()
    return redirect(displaysignup)

