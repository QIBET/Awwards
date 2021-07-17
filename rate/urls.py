from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns=[
    url('^$',views.index,name='index'),
    url('register/', views.register, name="register"),
	url('login/', views.loginUser, name="login"), 
    url('logout/',views.logoutUser,name="logout") ,
    url(r'^profile/$', views.profile,name='profile'),
    url(r'^edit/$',views.profile_update,name='edit'),
]
