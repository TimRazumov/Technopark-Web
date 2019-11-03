from django.urls import path
from .views import *

urlpatterns = [
    path('', questions_list, name='questions_list_url'),
    path('login/', login, name='login_url'),
    path('signup/', signup, name='signup_url'),
    path('question/<str:slug>/', question, name='question_url'),
    path('ask/', ask, name='ask_url'),
]
