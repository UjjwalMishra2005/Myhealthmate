from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('save_token/', views.save_token, name='save_token'),
    path('serve/', views.serve, name='serve'),
    path('get-doctors/', views.get_doctors, name='get_doctors'),

]