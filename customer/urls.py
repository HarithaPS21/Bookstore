from django.urls import path
from customer import views

urlpatterns=[
    path("accounts/signup",views.signup_view,name="signup"),
    path("accounts/signin",views.signin_view,name="signin"),
    path("accounts/signout",views.signout_view,name="signout"),
    path("",views.user_home,name="home"),
    path("books/orders/add/<int:id>",views.order_create,name="ordercreate"),
    path("books/orders",views.orders_list,name="orderslist"),
    path("books/orders/remove/<int:id>",views.cancel_order,name="cancelorder"),
    path("books/find",views.book_find,name="findbook")

]