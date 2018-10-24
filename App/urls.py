from django.conf.urls import url
from App import views

app_name = 'App'

urlpatterns = [
    url(r'^app/register/?$',views.register_user,name = 'register'),
    url(r'^app/user_login/?$',views.user_login,name = 'user_login'),
    url(r'^app/internships/?$',views.InternshipList.as_view(), name = 'internship_list'),
    url(r'^',views.index,name='index'),
]