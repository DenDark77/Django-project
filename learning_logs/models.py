from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """Teма, яку вивчає користувач"""
    text = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Повертає строкове уявлення моделі"""
        return self.text

class Entry(models.Model):
    """Информация, изученная пользователем по теме"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
    #Возвращает строковое представление модели.
        return f"{self.text[:50]}..."