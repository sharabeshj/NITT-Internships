from django.contrib import admin
from App.models import Profile,Profile_add_details,Profile_education,Profile_internships,Profile_POR,Profile_projects,Profile_skills,Profile_work_samples,Internship,Internship_sq,Professor,Application

# Register your models here.
admin.site.register(Profile)
admin.site.register(Profile_add_details)
admin.site.register(Profile_education)
admin.site.register(Profile_internships)
admin.site.register(Profile_POR)
admin.site.register(Profile_projects)
admin.site.register(Profile_skills)
admin.site.register(Profile_work_samples)
admin.site.register(Professor)
admin.site.register(Internship)
admin.site.register(Internship_sq)
admin.site.register(Application)

