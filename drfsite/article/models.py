from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок', default=None)
    content = models.TextField(blank=False, verbose_name='Текст статьи')
    time_created = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, verbose_name='Категория')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'
        ordering = ['-time_created', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']
