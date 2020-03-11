from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'core'

urlpatterns = [
    # Login
    # https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.views.LoginView
    path('login/', auth_views.LoginView.as_view(template_name='core/auth.html'), name='login'),

    # Logout
    # https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.views.LogoutView
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Dashboard
    path('', views.DashboardView.as_view(), name='dashboard'),

    # Users
    path('users/', views.UsersView.as_view(), name='list'),
    path('user/new', views.UserCreateView.as_view(), name='register'),
    path('user/<uuid:pk>', views.UserDetailView.as_view(), name='detail'),
    path('user/<uuid:pk>/edit', views.UserEditView.as_view(), name='edit'),
    path('user/<uuid:pk>/delete', views.user_delete_view, name='delete'),
]
