from django.conf.urls import url
from App import views

app_name = 'App'

urlpatterns = [
    url(r'^app/register/(?P<username>[0-9]+)/?$',views.register_user,name = 'register'),
    url(r'^app/user_login/?$',views.user_login,name = 'user_login'),
    url(r'^app/user_logout/?$',views.user_logout, name='user_logout'),
    url(r'^app/internships/?$',views.InternshipList.as_view(), name = 'internship_list'),
    url(r'^app/internship_detail/(?P<pk>[0-9]+)/?$',views.InternshipDetail.as_view(),name='internship-detail'),
    url(r'^app/professor_detail/(?P<pk>[0-9]+)/?$', views.ProfessorDetail.as_view(), name='professor-detail'),
    url(r'^dashboard/?$',views.index,name='index'),
    url(r'^$',views.home, name='home')
]