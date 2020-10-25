from django.urls import path
from . import views

urlpatterns = [
    path('post_search/', views.post_search, name = 'post_search'),
    path('post_search_detail/', views.post_search_detail, name='post_search_detail'),
    path('timeline/', views.timeline, name='timeline'),

    path('mypage/', views.mypage, name="mypage"),
    path('post_reservation/', views.post_reservation, name="post_reservation"),
    path('post_reserve_look/', views.post_reserve_look, name="post_reserve_look"),
    path('post_reserve_look_detail/<int:pk>', views.post_reserve_look_detail, name="post_reserve_look_detail"),
    path('post_reserve_delete', views.post_reserve_delete,name="post_reserve_delete"),
]