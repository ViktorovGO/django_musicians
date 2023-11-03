from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

class Musician(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Заголовок')
    slug = models.SlugField(max_length = 255, unique = True, db_index = True, verbose_name = 'URL')
    content = models.TextField(blank = False, verbose_name = 'Текст статьи')
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/', verbose_name = 'Фото') 
    time_create = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата создания')
    time_update = models.DateTimeField(auto_now = True, verbose_name = 'Дата обновления')
    is_published = models.BooleanField(default = True, verbose_name = 'Опубликовано')
    cat = models.ForeignKey('Category', on_delete = models.PROTECT, verbose_name = 'Жанр')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('posts:post', kwargs = {'post_slug':self.slug})
    
    class Meta:
        verbose_name = 'Музыкант'
        verbose_name_plural = 'Музыканты'
        ordering = ['-time_create']

class Category(models.Model):
    name = models.CharField(max_length = 100, db_index = True, verbose_name = 'Жанр')
    slug = models.SlugField(max_length = 255, unique = True, db_index = True, verbose_name = 'URL')
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('posts:category', kwargs = {'cat_slug':self.slug})
   
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']

class Comment(models.Model):
    post = models.ForeignKey(Musician, on_delete=models.CASCADE, verbose_name = 'Пост')
    content = models.TextField(blank = False, verbose_name = 'Текст комментария')
    time_create = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата создания')
    time_update = models.DateTimeField(auto_now = True, verbose_name = 'Дата обновления')
    is_published = models.BooleanField(default = True, verbose_name = 'Опубликовано')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-time_create']