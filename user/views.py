from django.shortcuts import render,redirect
from django.contrib.auth.models import  auth,User
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import tbl_student_form
from .models import tbl_student
from django.db.models import Q


def home(request):
    return render(request,'home.html')

def signupuser(request):
    if(request.method=='GET'):
        return render(request,'signupuser.html')
    else:
        username=request.POST['username']
        pwd1=request.POST['password1']
        pwd2=request.POST['password2']
        User = get_user_model()
        if(pwd1==pwd2):
            if(User.objects.filter(username=username).exists()):
                messages.error(request,'username exists')
                return redirect('signupuser')
            else:
                user=User.objects.create_user(username=username,password=pwd1)
                user.save()
                login(request,user)
        else:
            messages.error(request,'password not matching')
            return redirect('signupuser')
        return redirect('home')


def loginuser(request):
    if(request.method=='GET'):
        return render(request,'loginuser.html')
    else:
        username=request.POST['username']
        password=request.POST['password']
        User = get_user_model()
        try:
            user=auth.authenticate(username=username,password=password)
            if(User is not None):
                auth.login(request, user)
                return redirect('home')
        except AttributeError:
            messages.warning(request,'Invalid credentials.Please try again')
            return redirect('loginuser')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def fillupform(request):
    if(request.method=='GET'):
        form = tbl_student_form()
        return render(request,'fillupform.html',{'form':form})
    else:
        form = tbl_student_form(request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect('/hooray')
        else:
            return render(request,'fillupform.html',{'form':form})

@login_required
def displayform(request):
    student_forms = tbl_student.objects.all()
    print(f'student_forms -> {student_forms}')
    return render(request,'displayform.html',{'student_forms':student_forms})
    

def success(request):
    return render(request,'success.html')


def searchform(request):
    if(request.method=='POST'):
        search_term=request.POST['search_term']
        lookups= Q(student_name__icontains=search_term) | Q(college_name__icontains=search_term) | Q(internship_applied__icontains=search_term) | Q(email_id__icontains=search_term) |Q(degree_name__icontains=search_term) | Q(specialisation__icontains=search_term)
        search_results = tbl_student.objects.filter(lookups).distinct()
        return render(request,'displayform.html',{'student_forms':search_results})

