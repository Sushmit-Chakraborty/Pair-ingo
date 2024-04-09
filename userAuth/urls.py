from django.urls import path
from . import views

urlpatterns = [
     path('register',views.registerUser,name='registerUser'),
     path('login',views.loginUser,name='loginUser'),
     path('techStack',views.addTech,name='addTech'),
     path('homePage',views.homePage,name='homePage'),
     path('logout',views.logoutUser,name='logout')
]
