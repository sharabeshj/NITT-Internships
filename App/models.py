from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator,MaxValueValidator,MinValueValidator

import datetime

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User,related_name = 'base_profile', on_delete = models.CASCADE)
    interned = models.BooleanField(default = False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile = models.CharField(validators = [phone_regex],max_length = 17, blank = True)
    resume = models.FileField(null = True)
    cover_letter = models.FileField(null = True)
    lor = models.FileField(null = True)

def current_year():
    return datetime.date.today().year
    
def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

def max_value_end_year(value):
    return MaxValueValidator(current_year()+6)(value)

class Profile_education(models.Model):

    user = models.ForeignKey(User,related_name='profile_education',on_delete = models.CASCADE)
    graduation_status_choices = (('P','Pursuing'),('C','Completed'))
    graduation_status = models.CharField(max_length = 1,choices = graduation_status_choices)
    college = models.CharField(max_length = 200)
    start_year = models.IntegerField(validators=[MinValueValidator(1984), max_value_current_year])
    end_year = models.IntegerField(validators=[MinValueValidator(1984),max_value_current_year])
    degree = models.CharField(max_length = 100)
    stream = models.CharField(max_length = 50)
    cgpa = models.FloatField(validators=[MaxValueValidator(10)])

class Profile_internships(models.Model):

    user = models.ForeignKey(User,related_name='profile_internships',on_delete = models.CASCADE)
    profile = models.CharField(max_length = 50)
    organization = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

class Profile_POR(models.Model):

    user = models.ForeignKey(User,related_name='profile_por',on_delete = models.CASCADE)
    description = models.TextField()

class Profile_projects(models.Model):

    user = models.ForeignKey(User,related_name='profile_projects',on_delete = models.CASCADE)
    title = models.CharField(max_length = 50)
    start_month = models.DateField()
    end_month = models.DateField()
    description = models.TextField()
    project_link = models.URLField()

class Profile_skills(models.Model):

    user = models.ForeignKey(User,related_name='profile_skills',on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    level_choices = (('B','Beginner'),('I','Intermediate'),('A','Advanced'))
    level = models.CharField(max_length = 1, choices = level_choices)

class Profile_work_samples(models.Model):

    user = models.ForeignKey(User,related_name='profile_work_samples',on_delete = models.CASCADE)
    blog_link = models.URLField()
    github_profile = models.URLField()
    other_portfolio_link = models.URLField()

class Profile_add_details(models.Model):

    user = models.ForeignKey(User,related_name='profile_add_details',on_delete = models.CASCADE)
    add_details = models.TextField()

class Professor(models.Model):

    name = models.CharField(max_length = 50)
    bio = models.TextField()

class Internship(models.Model):

    professor = models.ForeignKey(Professor,related_name='interships',on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    description = models.TextField()
    stipend = models.IntegerField(blank=True)
    number_of_internships = models.IntegerField()
    start_date = models.DateField()
    duration = models.IntegerField()
    posted_on = models.DateField()
    apply_by = models.DateField()
    incentives = models.TextField()

class Internship_sq(models.Model):

    internship = models.ForeignKey(Internship,related_name='internship_sq',on_delete = models.CASCADE)
    question = models.CharField(max_length = 100)
    answer = models.TextField()

class Application(models.Model):

    internship = models.ForeignKey(Internship,related_name='application',on_delete = models.CASCADE)
    user = models.ManyToManyField(User,related_name='applications')
