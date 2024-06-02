from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('accounts/', views.account_list, name='account_list'),
    path('account/<int:pk>/', views.account_detail, name='account_detail'),
    path('account/new/', views.account_create, name='account_create'),
    path('account/<int:pk>/edit/', views.account_edit, name='account_edit'),
    path('account/<int:pk>/delete/', views.account_delete, name='account_delete'),
    path('surveys/', views.survey_list, name='survey_list'),
    path('survey/<int:pk>/', views.survey_detail, name='survey_detail'),
]
