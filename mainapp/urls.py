from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name = 'main'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
]
