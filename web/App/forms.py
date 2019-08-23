from django import forms
from django.contrib.auth.models import User
from App.models import Profile, Profile_education, Profile_projects, Profile_POR, Profile_skills, Profile_internships, \
    Profile_add_details, Profile_work_samples


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class ProfileEducationForm(forms.ModelForm):
    class Meta:
        model = Profile_education
        exclude = ('profile',)


class ProfileProjectsForm(forms.ModelForm):
    class Meta:
        model = Profile_projects
        exclude = ('profile',)


class ProfilePORForm(forms.ModelForm):
    class Meta:
        model = Profile_POR
        exclude = ('profile',)


class ProfileSkillsForm(forms.ModelForm):
    class Meta:
        model = Profile_skills
        exclude = ('profile',)


class ProfileInternshipForm(forms.ModelForm):
    class Meta:
        model = Profile_internships
        exclude = ('profile',)


class ProfileAddDetailsForm(forms.ModelForm):
    class Meta:
        model = Profile_add_details
        exclude = ('profile',)


class ProfileWorkSampleForm(forms.ModelForm):
    class Meta:
        model = Profile_work_samples
        exclude = ('profile',)
