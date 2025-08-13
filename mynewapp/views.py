import random
from datetime import datetime
from multiprocessing.synchronize import Event

import smtplib
import ssl
from email.mime.text import MIMEText

from django.conf import settings
from django.contrib.auth import authenticate,logout,login
from django.core.mail import send_mail
from django.db.models.fields import return_None

from .models import User, book, Admin
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages

from django.contrib import messages
from django.shortcuts import render, redirect

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


# ... (rest of your imports and views)

def edit_page(request):
    # Check if 'u_name' exists in the session
    uname = request.session.get("u_name")

    if not uname:
        return redirect("login")

    # Get the user object using the username from the session
    try:
        data = User.objects.get(uname=uname)
    except User.DoesNotExist:
        # Handle the case where the user is not found, although this should be rare
        messages.error(request, "User not found.")
        return redirect("login")

    locate = {"data": data}
    return render(request, "edit_page.html", locate)


def update(request):
    if request.method == "POST":
        uname = request.session.get("u_name")  # Get username from the session, not the form
        if not uname:
            return redirect("login")

        try:
            user_to_update = User.objects.get(uname=uname)
            user_to_update.email = request.POST.get("email")
            user_to_update.contact = request.POST.get("contact")
            user_to_update.save()
            messages.success(request, "Your profile has been updated!")
            return redirect("profile")  # Redirect to the profile page to see changes

        except User.DoesNotExist:
            messages.error(request, "User not found.")
            return redirect("login")

    return redirect("edit_page")


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

        # Fetch all orders from the book table
        orders = book.objects.all()

        locate = {
            "name": aname,
            "data": orders
        }
        return render(request, "adminhome.html", locate)
    else:
        locate = {"status": "You need to login first"}
        return render(request, "adminhome.html", locate)
def admin_logout(request):
    if 'a_name' in request.session:
        del request.session['a_name']
        return render(request,"admin_login.html")


    else:
        locate={'status':'you need to login first'}
        return render(request,"admin_login.html",locate)

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
        return render(request, "thankyou.html", locate)

    else:
        today = datetime.today().date().isoformat()
        # Query se book name aur price le rahe hain
        book_name = request.GET.get("book_name", "")
        price = request.GET.get("price", "")

        locate = {
            "user_name": user.uname,
            "user_contact": user.contact,
            "user_email": user.email,
            "msg": "",
            "status": "",
            "date": today,
            "book_name": book_name,
            "price": price
        }
        return render(request, "read_book.html", locate)

def delete_order(request):
    if 'a_name' in request.session:
        id=request.GET.get("id")
        book.objects.filter(bid=id).delete()
        record = book.objects.all()
        locate = {"data": record, "msg": "Employee Deleted"}
        return render(request, "admin_book.html", locate)


    else:
        locate={"status":"you need to login"}
        return render(request,"admin_login.html",locate)

def mail_send(request):
        return render(request,"email_form.html")


def email_check(request):
    if request.method == "POST":
        email = request.POST.get("email")
        otp = random.randint(1000, 9999)

        # Store in session for later
        request.session["otp"] = str(otp)
        request.session["reset_email"] = email

        subject = "Forget Password"
        body = f"Your OTP is: {otp}"
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = settings.EMAIL_HOST_USER
        msg["To"] = email

        context = ssl._create_unverified_context()

        try:
            with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
                server.starttls(context=context)
                server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
                server.send_message(msg)

            # After sending mail → show OTP entry page
            return render(request, "enter_otp.html", {"msg": "Email sent successfully!"})

        except Exception as e:
            return render(request, "enter_otp.html", {"msg": f"Error: {e}"})

    return render(request, "enter_email.html")

def otp_check(request):
    if request.method == "POST":
        entered_otp = request.POST.get("otp")  # from form input
        saved_otp = request.session.get("otp")  # from session

        if str(entered_otp) == str(saved_otp):
            return render(request, "update_pass.html")
        else:
            return render(request, "enter_otp.html", {"msg": "Wrong OTP"})
    return render(request, "enter_otp.html")



def update_pass(request):
    if request.method == "POST":
        new_pass = request.POST.get("new_password")
        confirm_pass = request.POST.get("confirm_password")
        email = request.session.get("reset_email")  # get email stored during OTP step

        if new_pass != confirm_pass:
            return render(request, "update_pass.html", {"msg": "Passwords do not match."})

        if email:
            try:
                user = User.objects.get(email=email)
                user.password = new_pass  # if storing raw password (bad practice) or hash it properly
                user.save()

                # Clear reset session data
                request.session.pop("reset_email", None)
                request.session.pop("otp", None)

                messages.success(request, "Password updated successfully. Please login.")
                return redirect("login")  # your login page name

            except User.DoesNotExist:
                return render(request, "update_pass.html", {"msg": "User not found."})
        else:
            return render(request, "update_pass.html", {"msg": "Session expired. Restart the process."})

    return render(request, "update_pass.html")


def thankyou(request):
    return render(request,"thankyou.html")