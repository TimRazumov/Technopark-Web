# Generated by Django 2.2.6 on 2019-11-04 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('avatar', models.ImageField(upload_to='static/img/avatars/')),
                ('date', models.DateField(null=True, verbose_name='День Рождения')),
                ('num_like', models.IntegerField(default=0, verbose_name='Количество лайков')),
                ('num_dislike', models.IntegerField(default=0, verbose_name='Количество дизлайков')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('body', models.TextField(blank=True, verbose_name='Текст')),
                ('datetime_published', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('num_like', models.IntegerField(default=0, verbose_name='Количество лайков')),
                ('num_dislike', models.IntegerField(default=0, verbose_name='Количество дизлайков')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bomonka_forum.Profile', verbose_name='Автор')),
                ('dislike', models.ManyToManyField(blank=True, related_name='questions_dislike', to='bomonka_forum.Profile', verbose_name='Дизлайки')),
                ('like', models.ManyToManyField(blank=True, related_name='questions_like', to='bomonka_forum.Profile', verbose_name='Лайки')),
                ('tags', models.ManyToManyField(blank=True, related_name='questions_tags', to='bomonka_forum.Tag', verbose_name='Тэги')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ['-datetime_published'],
                'unique_together': {('title', 'body')},
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(null=True, verbose_name='Текст')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('correctness', models.BooleanField(default=False, verbose_name='Правильность')),
                ('num_like', models.IntegerField(default=0, verbose_name='Количество лайков')),
                ('num_dislike', models.IntegerField(default=0, verbose_name='Количество дизлайков')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bomonka_forum.Profile')),
                ('dislike', models.ManyToManyField(blank=True, related_name='answers_dislike', to='bomonka_forum.Profile', verbose_name='Дизлайки')),
                ('like', models.ManyToManyField(blank=True, related_name='answers_like', to='bomonka_forum.Profile', verbose_name='Лайки')),
                ('questions', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='bomonka_forum.Question', verbose_name='Вопросы')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
