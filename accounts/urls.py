from django.urls import path
from .import views


urlpatterns = [
    path('login/',views.login, name = 'login'),
    path('ku/login/',views.login, name = 'loginKu'),
    path('ar/login/',views.login, name = 'loginAr'),
    path('register/',views.register, name = 'register'),
    path('ku/register/',views.register, name = 'registerKu'),
    path('ar/register/',views.register, name = 'registerAr'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('ku/dashboard/', views.dashboard, name = 'dashboardKu'),
    path('ar/dashboard/', views.dashboard, name = 'dashboardAr'),
    path('withdrawl/', views.withdrawl, name = 'withdrawl'),
    path('ku/withdrawl', views.withdrawl, name = 'withdrawlKu'),
    path('ar/withdrawl/', views.withdrawl, name = 'withdrawlAr'),
    path('logout/', views.logout, name = 'logout'),
    path('ku/logout/', views.logout, name = 'logoutKu'),
    path('ar/logout/', views.logout, name = 'logoutAr'),
    # path('password/reset/', views.password_reset_func, name = 'password_reset'),
    # path('password/reset/done/<slug:token>', views.password_reset_done, name = 'password_reset_done'),
]