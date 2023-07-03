from django.urls import path
from . import views



urlpatterns = [
    
    path('',views.home,name='home'),
    path('sign_in',views.sign_in,name='login'),
    path('user_dashboard/',views.user_dashboard,name='user_dashboard'),
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.create_user, name='user_create'),
    path('users/<str:username>/', views.user_detail, name='user_detail'),
    path('users/<str:username>/update/', views.user_update, name='user_update'),
    path('users/<str:username>/delete/', views.user_delete, name='user_delete'),

    path('profiles/', views.profile_list, name='profile_list'),
    path('profiles/create/', views.profile_create, name='profile_create'),
    path('profiles/<str:username>/', views.profile_detail, name='profile_detail'),
    path('profiles/<str:username>/update/', views.profile_update, name='profile_update'),
    path('profiles/<str:username>/delete/', views.profile_delete, name='profile_delete'),

    path('posts/', views.post_list, name='post_list'),
    path('posts/create/', views.create_post, name='post_create'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/<int:post_id>/update/', views.post_update, name='post_update'),
    path('posts/<int:post_id>/delete/', views.post_delete, name='post_delete'),
]
