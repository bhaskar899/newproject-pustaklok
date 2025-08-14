
from django.contrib import admin
from django.urls import path,include

from .import views

urlpatterns = [

    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("register/",views.register,name="register"),
    path("logout_page/",views.logout_page,name="logout_page"),
    path("edit_page/",views.edit_page,name="edit_page"),
    path("update/",views.update,name="update"),
    path("user_data/", views.user_data, name="user_data"),
    path("login/",views.login,name="login"),
    path("user_login/", views.user_login, name="user_login"),

    # path("read_book/", views.read_book, name="read_book"),

    path("book_book/", views.book_book, name="book_book"),
    path("admin_login_page/", views.admin_login_page, name="admin_login_page"),
    path("admin_check/",views.admin_check,name="admin_check"),
    path("admin_book/", views.admin_book, name="admin_book"),
    path("contact/", views.contact, name="contact"),
    path("profile/", views.profile_view, name="profile"),
    path("userhome/",views.userhome,name="userhome"),
    path("admin_logout/",views.admin_logout,name="admin_logout"),
    path("delete_order/",views.delete_order,name="delete_order"),

    # order book

    path("buy_now/",views.buy_now,name="buy_now"),

    # About pages

    path("about1/", views.about1, name="about1"),
    path("about2/",views.about2,name="about2"),
    path("about3/",views.about3,name="about3"),
    path("about4/",views.about4,name="about4"),
    path("about5/",views.about5,name="about5"),
    path("about6/",views.about6,name="about6"),
    path("about7/",views.about7,name="about7"),
    path("about8/",views.about8,name="about8"),
    path("about9/",views.about9,name="about9"),
    path("about10/",views.about10,name="about10"),

    path("about11/", views.about11, name="about11"),
    path("about12/", views.about12, name="about12"),
    path("about13/", views.about13, name="about13"),
    path("about14/", views.about14, name="about14"),
    path("about15/", views.about15, name="about15"),
    path("about16/", views.about16, name="about16"),
    path("about17/", views.about17, name="about17"),
    path("about18/", views.about18, name="about18"),
    path("about19/", views.about19, name="about19"),
    path("about20/", views.about20, name="about20"),

    path("about21/", views.about21, name="about21"),
    path("about22/", views.about22, name="about22"),
    path("about23/", views.about23, name="about23"),
    path("about24/", views.about24, name="about24"),
    path("about25/", views.about25, name="about25"),
    path("about26/", views.about26, name="about26"),
    path("about27/", views.about27, name="about27"),
    path("about28/", views.about28, name="about28"),

    path("about29/", views.about29, name="about29"),
    path("about30/", views.about30, name="about30"),
    path("about31/", views.about31, name="about31"),
    path("about32/", views.about32, name="about32"),
    path("about33/", views.about33, name="about33"),
    path("about34/", views.about34, name="about34"),
    path("about35/", views.about35, name="about35"),
    path("about36/", views.about36, name="about36"),

#     Cart add message
    path("add_to_cart/<int:book_id>/",views.add_to_cart,name="add_to_cart"),

#     mail sending
    path("mail_send/", views.mail_send, name="mail_send"),
    path("email_check/", views.email_check, name="email_check"),
    path("otp_check/", views.otp_check, name="otp_check"),
    path("update_pass/<int:id>/", views.update_pass, name="update_pass"),

#     thank you
    path("thankyou/",views.thankyou,name="thankyou.html")

]
