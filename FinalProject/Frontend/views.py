from django.shortcuts import render,redirect
from Finalapp.models import CategoryDb,ProductDb,ContactDb
from Frontend.models import ReservationDb,SignupDb,CartDb,CheckoutDb
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

# Create your views here.
def homepage(request):
    category = CategoryDb.objects.all()
    return render(request, "Home.html", {'category':category})
def menupage(request):
    pro = ProductDb.objects.all()
    return render(request, "Menu_all.html", {'pro':pro})

def reservationpage(request):
    return render(request, "Reservation.html")
def reservationdata(request):
    if request.method == "POST":
        da = request.POST.get('date')
        ti = request.POST.get('time')
        pe = request.POST.get('people')
        na = request.POST.get('name')
        un = request.POST.get('uname')
        ph = request.POST.get('phone')
        em = request.POST.get('email')
        obj = ReservationDb(Date=da, Time=ti, Person=pe, Name=na, Phone=ph, Email=em, Username=un)
        obj.save()
        email_message = render_to_string('EmailReservation_sender.html', {
            'name': na,
            'phone': ph,
            'email': em,
            'date': da,
            'time': ti,
            'persons': pe,
        })

        send_mail(
            subject='Table Reserved Successfully..!',
            message='',
            from_email=settings.DEFAULT_FROM_EMAIL,  # Set your default 'from' email in settings.py
            recipient_list=[settings.CONTACT_EMAIL],  # Set the recipient email address in settings.py
            html_message=email_message,
        )
        messages.success(request, "Table Reserved Successfully..!")
        return redirect(reservationpage)
def Gallerypage(request):
    return render(request, "Gallery_Pic.html")
def aboutpage(request):
    return render(request, "About.html")
def contactpage(request):
    return render(request, "Contact.html")
def contactdetails(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('mail')
        ph = request.POST.get('mobile')
        mes = request.POST.get('message')
        obj = ContactDb(Name=na, EmailId=em, Phone=ph, Message=mes)
        obj.save()
        email_message = render_to_string('Email_send.html', {
            'message_name': na,
            'message_email': em,
            'message': mes,
        })

        send_mail(
            subject='Your Message Received Successfully..!',
            message=mes,
            from_email=settings.DEFAULT_FROM_EMAIL,  # Set your default 'from' email in settings.py
            recipient_list=[settings.CONTACT_EMAIL],  # Set the recipient email address in settings.py
            html_message=email_message,
        )

        messages.success(request, "Message Sent")
        return redirect(contactpage)

def menufilteredpage(request, cat_name):
    filtered = ProductDb.objects.filter(Category_Name=cat_name)
    return render(request, "FilteredMenu.html", {'filtered':filtered})
def singleproduct(request, productid):
    product = ProductDb.objects.get(id=productid)
    return render(request, "SingleItem.html", {'product':product})
def loginpage(request):
    return render(request, "Signin.html")
def signupdata(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('mail')
        mob = request.POST.get('phone')
        un = request.POST.get('uname')
        pwd = request.POST.get('password')
        rpwd = request.POST.get('rpassword')
        obj = SignupDb(Name=na, EmailId=em, Mobile=mob, UserName=un, Password=pwd, RepeatedPassword=rpwd)
        obj.save()
        return redirect(loginpage)
def userlogin(request):
    if request.method == "POST":
        un = request.POST.get('user_name')
        pwd = request.POST.get('pass_word')
        if SignupDb.objects.filter(UserName=un, Password=pwd).exists():
            request.session['UserName']=un
            request.session['Password']=pwd
            return redirect(homepage)
        else:
            return redirect(loginpage)
    else:
        return redirect(loginpage)

def userlogout(request):
    del request.session['UserName']
    del request.session['Password']
    messages.success(request, "Logout Successfully..!")
    return redirect(loginpage)
def cartpage(request):
    data = CartDb.objects.filter(UserName=request.session['UserName'])
    total_price = 0
    for i in data:
        total_price = total_price + i.TotalPrice
    return render(request, "Cart.html",{'data':data,'total_price':total_price})
def cartdetails(request):
    if request.method == "POST":
        un = request.POST.get('user_name')
        pn = request.POST.get('productname')
        qu = request.POST.get('quantity')
        to = request.POST.get('totalprice')
        obj = CartDb(UserName=un, ProductName=pn, Quantity=qu, TotalPrice=to)
        obj.save()
        return redirect(cartpage)
def deletecartdetail(request,cartid):
    cart = CartDb.objects.filter(id=cartid)
    cart.delete()
    return redirect(cartpage)
def orderpage(request):
    data = CartDb.objects.filter(UserName=request.session['UserName'])
    messages.success(request, "order placed Successfully..!")
    return render(request, "Myorders.html",{'data':data})


def checkoutdata(request):
    if request.method == "POST":
        na = request.POST.get('name')
        mob = request.POST.get('phone')
        em = request.POST.get('mail')
        ad = request.POST.get('address')

        items_in_cart = CartDb.objects.all()

        checkout_obj = CheckoutDb(Name=na, Mobile=mob, Email=em, Address=ad)
        checkout_obj.save()

        checkout_obj.Items.set(items_in_cart)



        return redirect(orderpage)



