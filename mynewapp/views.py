from datetime import datetime
from django.contrib.auth import authenticate,logout,login
from .models import User, book, Admin
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def index(request):
    return render(request,"index.html")


def contact(request):
    return render(request,"contact.html")

def register(request):
    return render(request,"register.html")


# about views

def about1(request):
    return render(request,"about1.html")

def about2(request):
    return render(request,"about2.html")

def about3(request):
    return render(request,"about3.html")

def about4(request):
    return render(request,"about4.html")

def about5(request):
    return render(request,"about5.html")

def about6(request):
    return render(request,"about6.html")

def about7(request):
    return render(request,"about7.html")

def about8(request):
    return render(request,"about8.html")

def about9(request):
    return render(request,"about9.html")

def about10(request):
    return render(request,"about10.html")

def about11(request):
    return render(request,"about11.html")

def about12(request):
    return render(request,"about12.html")

def about13(request):
    return render(request,"about13.html")

def about14(request):
    return render(request,"about14.html")

def about15(request):
    return render(request,"about15.html")

def about16(request):
    return render(request,"about16.html")

def about17(request):
    return render(request,"about17.html")

def about18(request):
    return render(request,"about18.html")

def about19(request):
    return render(request,"about19.html")

def about20(request):
    return render(request,"about20.html")

def about21(request):
    return render(request,"about21.html")

def about22(request):
    return render(request,"about22.html")

def about23(request):
    return render(request,"about23.html")

def about24(request):
    return render(request,"about24.html")

def about25(request):
    return render(request,"about25.html")

def about26(request):
    return render(request,"about26.html")

def about27(request):
    return render(request,"about27.html")

def about28(request):
    return render(request,"about28.html")

def about29(request):
    return render(request,"about29.html")

def about30(request):
    return render(request,"about30.html")

def about31(request):
    return render(request,"about31.html")

def about32(request):
    return render(request,"about32.html")

def about33(request):
    return render(request,"about33.html")

def about34(request):
    return render(request,"about34.html")

def about35(request):
    return render(request,"about35.html")

def about36(request):
    return render(request,"about36.html")




def user_data(request):
    if request.method=="POST":
        name=request.POST.get("uname")
        email=request.POST.get("email")
        gender=request.POST.get("gender")
        password=request.POST.get("password")
        contact=request.POST.get("contact")

        record=User(uname=name,email=email,gender=gender,password=password,contact=contact)
        record.save()

        locate={"msg":"User Created Successfully"}
        return render(request,"register.html",locate)
    return None

def login(request):
    if 'u_name' in request.session:
        locate = {"name": request.session.get('u_name')}
        return render(request, "userhome.html", locate)

    return render(request, "login.html")


def logout_page(request):
    request.session.flush()
    return redirect("login")


def user_login(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        password = request.POST.get("password")

        try:
            user = User.objects.get(uname=uname)
            if user.password == password:
                request.session["u_name"] = uname
                return userhome(request)
            else:
                locate = {"msg": "Password incorrect"}
                return render(request, "login.html", locate)

        except User.DoesNotExist:
            locate = {"msg": "Username incorrect"}
            return render(request, "login.html", locate)

    # If request is not POST, just return the login page
    return render(request, "login.html")


def userhome(request):
    if "u_name" in request.session:
        uname=request.session.get("u_name")
        locate={"name":uname}
        return render(request,"userhome.html",locate)
    else:
        locate={"status":"You need to login first"}
        return render(request,"userhome.html",locate)


from .models import book, User  # make sure both are imported

def book_book(request):
    if request.method == 'POST':
        date = request.POST.get("date")
        time = request.POST.get("time")

        try:
            # Check if the slot is already booked (optional logic)
            bookread = book.objects.get(date=date, time=time)
            locate = {"msg": "Please select another date/time"}
            return render(request, "read_book.html", locate)

        except book.DoesNotExist:
            # Get the logged-in user
            user = User.objects.get(uname=request.session.get('u_name'))

            # Now create a new booking record using the book model
            bookread = book(
                uid=user.uid,
                name=user.uname,
                date=date,
                time=time,
                mobile=user.contact
            )
            bookread.save()

            locate = {"status": "Booking Successfully"}
            return render(request, "read_book.html", locate)

    else:
        locate = {"msg": "Something went wrong"}
        return render(request, "read_book.html", locate)



def admin_login_page(request):
    if 'a_name' in request.session:
        locate={"name":request.session.get('a_name')}
        return render(request,"adminhome.html",locate)

    return render(request,"admin_login.html")

def admin_check(request):
    if request.method == "POST":
        aname = request.POST.get("aname")
        password = request.POST.get("password")

        try:
            bhaskar = Admin.objects.get(name=aname)

            if bhaskar.password==password:
                request.session["a_name"] = aname
                return adminhome(request)

            else:
                locate = {"msg": "Password incorrect"}
                return render(request, "admin_login.html", locate)

        except Admin.DoesNotExist:
            locate = {"msg": "Username incorrect"}
            return render(request, "admin_login.html", locate)

        # If request is not POST, just return the login page
    return render(request, "admin_login.html")


def adminhome(request):
    if "a_name" in request.session:
        aname = request.session.get("a_name")
        locate = {"name": aname}
        return render(request, "adminhome.html", locate)
    else:
        locate = {"status": "You need to login first"}
        return render(request, "adminhome.html", locate)

def admin_book(request):
    if 'a_name' in request.session:
        booking=book.objects.all()
        locate={'data':booking}
        return render(request,"admin_book.html",locate)


    else:
        locate={"status":"you need to login first"}
        return render(request,"login.html",locate)


def profile_view(request):
    if "u_name" in request.session:
        uname = request.session.get("u_name")
        try:
            user = User.objects.get(uname=uname)
            locate = {
                "user": user
            }
            return render(request, "profile.html", locate)
        except User.DoesNotExist:
            return render(request, "login.html", {"msg": "User not found"})

    return redirect("login")



def add_to_cart(request,book_id):
    messages.success(request,"Book Added To Cart Successfully!")
    return redirect('/userhome/')

# order book

def buy_now(request):
    if "u_name" not in request.session:
        return render(request, "login.html", {"status": "You need to login first"})

    user = User.objects.get(uname=request.session["u_name"])

    if request.method == 'POST':
        book_name = request.POST.get("book_name")
        quantity = int(request.POST.get("quantity"))
        address = request.POST.get("address")
        date = request.POST.get("date")
        time = request.POST.get("time")
        mobile = request.POST.get("mobile")
        total_price = int(request.POST.get("total_price"))

        # Save order
        order = book(
            uid=user.uid,
            book_name=book_name,
            quantity=quantity,
            address=address,
            date=date,
            time=time,
            mobile=mobile,
            total_price=total_price,
        )
        order.save()
        locate = {
            "status": "Order placed successfully!",
            "user_name": user.uname,
            "user_contact": user.contact,
            "user_email": user.email,
            "date": datetime.today().date().isoformat(),
        }
        return render(request, "read_book.html", locate)

    else:
        today = datetime.today().date().isoformat()
        locate = {
            "user_name": user.uname,
            "user_contact": user.contact,
            "user_email": user.email,
            "msg": "",
            "status": "",
            "date": today,
        }
        return render(request, "read_book.html", locate)