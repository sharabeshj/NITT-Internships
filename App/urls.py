from django.conf.urls import url
from App import views

app_name = 'App'

urlpatterns = [
    url(r'^register/$',views.register_user,name = 'register'),
    url(r'^user_login/$',views.user_login,name = 'user_login')
]