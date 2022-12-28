from django.urls import path
from user import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),
    path('contact', views.contact, name='contact'),
    path('enroll', views.enroll, name='enroll'),
    path('profile', views.profile, name='profile'),
    




    

]