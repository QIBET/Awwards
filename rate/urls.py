from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import include

from . import views

urlpatterns=[
    url('^$',views.index,name='index'),
    url('register/', views.register, name="register"),
	url('login/', views.loginUser, name="login"), 
    url('logout/',views.logoutUser,name="logout") ,
    url(r'^profile/$', views.profile,name='profile'),
    url(r'^edit/$',views.profile_update,name='edit'),
    url(r'^project/$', views.project_post,name='uploadProject'),
    url(r'^search/', views.search_results, name='search'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^api/projects/$', views.ProjectsList.as_view()),
    url(r'ratings/', include('star_ratings.urls', namespace='ratings')),

]
