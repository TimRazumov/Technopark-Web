from django.urls import path
from .views import *

urlpatterns = [
    path('', redirect_new),
    path('new/', questions_new, name='questions_new_url'),
    path('top/', questions_top, name='questions_top_url'),
    path('tag/<str:title>/', questions_tag, name='question_tag_url'),
    path('login/', login, name='login_url'),
    path('signup/', signup, name='signup_url'),
    path('question/<str:slug>/', question_info, name='question_info_url'),
    path('ask/', ask, name='ask_url'),
]
