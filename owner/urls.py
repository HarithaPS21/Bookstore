from django.urls import path
from owner import views


urlpatterns=[
    path("", views.dashboard, name="dashboard"),
    path("dashboard/edit/<int:id>", views.dash_edit, name="dashedit"),
    path("books/", views.home, name="home"),
    path("books/add", views.book_create, name="addbook"),
    path("books/list", views.book_list, name="listbook"),
    path("books/change/<int:id>", views.book_update, name="changebook"),
    path("books/remove/<int:id>", views.book_remove, name="removebook"),
    path("accounts/signup", views.signupview, name="signup"),
    path("accounts/signin",views.signinview, name="signin"),
    path("books/details/<int:id>",views.book_detail, name="bookdetails")
]