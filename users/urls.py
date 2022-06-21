"""Схеми адрес для коритсувачів"""
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # Включає URL авторизацію за змовчуванням
    path('', include('django.contrib.auth.urls')),
    #Сторінка реєстрації
    path('register/', views.register, name='register'),
]