from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from App.models import Profile
from App.forms import UserForm,ProfileForm,LoginForm
from App.models import Internship
# Create your views here.

@login_required()
def index(request):

    return render(request,'App/home.html')

@login_required
def user_logout(request):

    logout(request)
    return HttpResponseRedirect(reverse('App:index'))

def register_user(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            return HttpResponse(user_form.errors)
    else:
        user_form = UserForm()
    
    return render(request,'App/user_registration.html',{
        'user_form' : user_form,
        'registered' : registered
    })



def user_login(request):

    if request.method == 'POST':

        user = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))


        if user is not None:
            if user.is_active:
                login(request,user)    
                return HttpResponseRedirect(reverse('App:index'))
            else:
                return HttpResponse("User is not active", status= 403)
        else:
            return HttpResponse("Invalid credentials", status= 403)
    else:
        return render(request,'App/login.html',{'login_form' : LoginForm})


class InternshipList(ListView):

    model = Internship

        
