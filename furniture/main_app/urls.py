from django.urls import path

from main_app.views import bed1_page, bedroom_page, cart_page, dine1_page, dine2_page, dine3_page, dine4_page, dine5_page, dine6_page, dining_page, home_page, login_page, signup_page, sofa_page

urlpatterns = [
    path("",home_page,name="home_page"),
    path("login",login_page,name="login_page"),
    path("signup",signup_page,name="signup_page"),
    path("bedroom",bedroom_page,name="bedroom_page"),
    path("dining",dining_page,name="dining_page"),
    path("sofa",sofa_page,name="sofa_page"),
    path("cart",cart_page,name="cart_page"),
    path("bed1",bed1_page,name="bed1_page"),
    path("dine1",dine1_page,name="dine1_page"),
    path("dine2",dine2_page,name="dine2_page"),
    path("dine3",dine3_page,name="dine3_page"),
    path("dine4",dine4_page,name="dine4_page"),
    path("dine5",dine5_page,name="dine5_page"),
    path("dine6",dine6_page,name="dine6_page"),

]
