'''from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from .models import *'''
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from .models import *

QUESTIONS_PER_PAGE = 3

def paginator(request, object_list, amount):
    paginator = Paginator(object_list, amount)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    next_url = ''
    
    if page.has_next():
        next_url = f'?page={page.next_page_number()}'

    prev_url = ''
    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'


    context = {
        'blogs': page,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url,
    }
    return context



'''
def questions_list(request):
    questions = Question.objects.show_new()
    context = paginator(request, questions, QUESTIONS_PER_PAGE)
    questions = range(0, 10)
    return render(request, 'bomonka_forum/index.html', context = {"questions": questions})

def login(request):
    return render(request, 'bomonka_forum/login.html', context = {})

def signup(request):
    return render(request, 'bomonka_forum/signup.html', context = {})

def question(request):
    return render(request, 'bomonka_forum/question.html', context = {})

def ask(request):
    return render(request, 'bomonka_forum/ask.html', context = {})'''
    
    


QUESTIONS_PER_PAGE = 3


def redirect_new(request):
    return redirect('questions_new_url', permanent=True)
    

def questions_new(request):
    questions = Question.objects.show_new()

    context = paginator(request, questions, QUESTIONS_PER_PAGE)
    return render(request, 'bomonka_forum/index.html', context=context)


def questions_top(request):
    search_query = request.GET.get('search', '')

    if search_query:
        questions = Question.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        questions = Question.objects.show_top()

    context = paginator(request, questions, QUESTIONS_PER_PAGE)
    return render(request, 'bomonka_forum/index.html', context=context)


def question_info(request, slug):
    q = get_object_or_404(Question, slug__iexact=slug)
    return render(request, 'bomonka_forum/question.html', context={'question': q})


def login(request):
    return render(request, 'bomonka_forum/login.html', context={})


def signup(request):
    return render(request, 'bomonka_forum/signup.html', context={})


def ask(request):
    return render(request, 'bomonka_forum/ask.html', context={})

'''
def tags(request):
    tags = Tag.objects.all()
    return render(request, 'bomonka_forum/tags.html', context={'tags': tags})


def tag_detail(request, title):
    t = Tag.objects.get(title__iexact=title)

    questions = t.questions.all()
    context = paginator(request, questions, QUESTIONS_PER_PAGE)

    context['tag'] = t
    return render(request, 'bomonka_forum/tag_detail.html', context)'''
