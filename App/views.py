from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from App.models import Profile
from App.forms import UserForm, ProfileForm, LoginForm, ProfileEducationForm, ProfileProjectsForm,ProfileSkillsForm,ProfileInternshipForm,ProfilePORForm,ProfileAddDetailsForm,ProfileWorkSampleForm
from App.models import Internship,Professor

import imaplib

# Create your views here.

def home(request):

    return render(request, 'App/homepage.html')

@login_required()
def index(request):

    return render(request, 'App/home.html')

@login_required
def user_logout(request):

    logout(request)
    return HttpResponseRedirect(reverse('App:index'))

def register_user(request,username):

    registered = False

    if request.method == 'POST':
        profile_form = ProfileForm(data = request.POST,prefix='basic')
        profile_education_form = ProfileEducationForm(data = request.POST,prefix='education')
        profile_internship_form = ProfileInternshipForm(data = request.POST,prefix='internship')
        profile_projects_form = ProfileProjectsForm(data = request.POST,prefix='project')
        profile_skill_form = ProfileSkillsForm(data = request.POST,prefix='skill')
        profile_por_form = ProfilePORForm(data = request.POST,prefix='por')
        profile_add_details_form = ProfileAddDetailsForm(data = request.POST,prefix='add_detail')
        profile_work_samples_form = ProfileWorkSampleForm(data = request.POST,prefix='work_samples')
        if profile_form.is_valid() and profile_education_form.is_valid() and profile_projects_form.is_valid() and profile_internship_form.is_valid() and profile_skill_form.is_valid() and profile_por_form.is_valid() and profile_add_details_form.is_valid() and profile_work_samples_form():
            user = User.objects.get(username=username)
            profile = profile_form.save(user=user)
            profile_education_form.cleaned_data['profile'] = profile
            profile_projects_form.cleaned_data['profile'] = profile
            profile_internship_form.cleaned_data['profile'] = profile
            profile_skill_form.cleaned_data['profile'] = profile
            profile_por_form.cleaned_data['profile'] = profile
            profile_add_details_form.cleaned_data['profile'] = profile
            profile_education_form.save()
            profile_projects_form.save()
            profile_internship_form.save()
            profile_skill_form.save()
            profile_por_form.save()
            profile_work_samples_form.save()
            profile_add_details_form.save()
            registered = True
        else:
            return HttpResponse(profile_form.errors)
    else:
        try:
            user = User.objects.get(username=username)
        except:
            return None

        profile_form = ProfileForm(prefix='basic')
        profile_education_form = ProfileEducationForm(prefix='education')
        profile_internship_form = ProfileInternshipForm(prefix='internship')
        profile_projects_form = ProfileProjectsForm(prefix='project')
        profile_skill_form = ProfileSkillsForm(prefix='skill')
        profile_por_form = ProfilePORForm(prefix='por')
        profile_add_details_form = ProfileAddDetailsForm(prefix='add_detail')
        profile_work_samples_form = ProfileWorkSampleForm(prefix='work_samples')
    
    return render(request, 'App/user_registration.html',{
        'profile_form': profile_form,
        'profile_education_form' : profile_education_form,
        'profile_projects_form' : profile_projects_form,
        'profile_internship_form' : profile_internship_form,
        'profile_skill_form' : profile_skill_form,
        'profile_por_form' : profile_por_form,
        'profile_add_details_form' : profile_add_details_form,
        'profile_work_samples_form' : profile_work_samples_form,
        'registered': registered
    })



def user_login(request):

    if request.method == 'POST':

        # user = authenticate(username = request.POST.get('username'), password = request.POST.get('password'))
        username = request.POST.get('username')
        password = request.POST.get('password')
        server_address = 'webmail.nitt.edu'
        print('came')
        try:
            M = imaplib.IMAP4(server_address)
            M.login(username, password)
            print('check')
        except:
            return HttpResponse('Invalid credentials', status=403)
        try:
            user = User.objects.get(username=username)
        except:
            user = User(username=username, is_staff=True, is_active=True, is_superuser=False)
            user.save()
            return HttpResponseRedirect(reverse('App:register', kwargs={'username': username}))
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('App:index'))
            else:
                return HttpResponse("User is not active", status= 403)
        else:
            return HttpResponse("Invalid credentials", status= 403)
    else:
        return render(request, 'App/login.html',{'login_form' : LoginForm})


class InternshipList(ListView):

    model = Internship

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = Internship.objects.count()
        return  context

class InternshipDetail(DetailView):

    model = Internship

class ProfessorDetail(DetailView):

    model = Professor
