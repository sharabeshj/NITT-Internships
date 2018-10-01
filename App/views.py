from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from App.models import Profile
from App.forms import UserForm,ProfileForm
# Create your views here.

def index(request):
    return render(request,'app/index.html')

@login_required
def user_logout(request):

    logout(request)
    return HttpResponseRedirect(reverse('index'))

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

        user = authenticate(username = request.username, password = request.password)

        if user is not None:
            if user.is_active:
                login(request,user)    
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("User is not active",status_code = 403)
        else:
            return HttpResponse("Invalid credentials",status_code = 403)       
    else:
        return render(request,'App/login.html',{})


        
