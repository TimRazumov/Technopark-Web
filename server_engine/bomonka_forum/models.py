# coding=utf-8
'''
    Пользователь – электронная почта, никнейм, пароль, аватарка, дата регистрации, рейтинг.
    Вопрос – заголовок, содержание, автор, дата создания, теги, рейтинг.
    Ответ – содержание, автор, дата написания, флаг правильного ответа, рейтинг.
    Тэг – слово тэга.
'''

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='static/img/avatars/', default='static/img/default_ava.jpg')
    date = models.DateField(null=True, verbose_name='День Рождения')
    
    '''
    TODO: сделать подсчет лайков и дизлайков по всем постам
    '''
    
    num_like = models.IntegerField(default=0, verbose_name='Количество лайков')
    num_dislike = models.IntegerField(default=0, verbose_name='Количество дизлайков')
    
    def __str__(self):
        return self.user.username
        
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

class QuestionManager(models.Manager):
    def show_new(self):
        return self.order_by('-datetime_published')

    def show_top(self):
        return self.order_by('-num_like')

class Question(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    body = models.TextField(blank=True, verbose_name='Текст')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Автор')
    datetime_published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    
    num_like = models.IntegerField(default=0, verbose_name='Количество лайков')
    num_dislike = models.IntegerField(default=0, verbose_name='Количество дизлайков')
    like = models.ManyToManyField('Profile', blank=True, related_name='questions_like', verbose_name='Лайки')
    dislike = models.ManyToManyField('Profile', blank=True, related_name='questions_dislike', verbose_name='Дизлайки')
    
    tags = models.ManyToManyField('Tag', blank=True, related_name='questions_tags', verbose_name='Тэги')

    slug = models.SlugField(max_length=150, unique=True)
    objects = QuestionManager()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['-datetime_published']
        unique_together = [('title'), ('body')]

class Answer(models.Model):
    body = models.TextField(null=True, verbose_name='Текст')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    correctness = models.BooleanField(default=False, verbose_name='Правильность')
    
    num_like = models.IntegerField(default=0, verbose_name='Количество лайков')
    num_dislike = models.IntegerField(default=0, verbose_name='Количество дизлайков')
    ''' можно ли сделать в админе выбор (имя юзера, лайк / дизлайк) ???'''
    like = models.ManyToManyField('Profile', blank=True, related_name='answers_like', verbose_name='Лайки')
    dislike = models.ManyToManyField('Profile', blank=True, related_name='answers_dislike', verbose_name='Дизлайки')
    
    questions = models.ForeignKey('Question', null=True, related_name='answers', verbose_name='Вопросы', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ['-num_like', '-num_dislike']

class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
