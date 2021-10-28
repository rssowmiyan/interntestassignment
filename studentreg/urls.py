from django.contrib import admin
from django.urls import path
from user import views
# I have a single app called 'user' to which I route my urls to users.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('signup/',views.signupuser,name='signupuser'),
    path('login/',views.loginuser,name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('fillup/',views.fillupform,name="fillupform"),
    path('hooray/',views.success,name="success"),
    path('display/',views.displayform,name="displayform"),
    path('search/',views.searchform,name="searchform")
]
