from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Домашня сторінка
    path('', views.index, name='index'),
    #Сторінка зі списком усіз тем
    path('topics/', views.topics, name='topics'),
    # Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #Сторінка для додатку нової теми
    path('new_topic/', views.new_topic, name='new_topic'),
    #Сторніка додавання нового запису
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #Редагування існуючих записів
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')
]