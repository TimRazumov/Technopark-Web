from django.shortcuts import render

def questions_list(request):
    return render(request, 'bomonka_forum/index.html', context={})

def login(request):
    return render(request, 'bomonka_forum/login.html', context={})

def signup(request):
    return render(request, 'bomonka_forum/signup.html', context={})

def question(request):
    return render(request, 'bomonka_forum/question.html', context={})

def ask(request):
    return render(request, 'bomonka_forum/ask.html', context={})
