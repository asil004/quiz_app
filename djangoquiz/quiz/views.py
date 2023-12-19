import random

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import CreateUserForm, AddQuestionForm
from .models import QuesModel


def home(request):
    if request.method == 'POST':
        question = QuesModel.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in question:
            if q.ans == request.POST.get(q.question):
                score += 10
                correct += 1
                total += 1
            else:
                wrong += 1
        if not total == 0:
            percent = correct / len(question) * 100
        else:
            percent = 0
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        return render(request, 'quiz/result.html', context)
    else:
        questions = QuesModel.objects.all()
        for q in questions:
            q.answer_choices = random.sample([q.op1, q.op2, q.op3, q.op4], 4)
        context = {
            'questions': questions
        }
        return render(request, 'quiz/home.html', context)


def add_question(request):
    if request.user.is_staff:
        form = AddQuestionForm()
        if request.method == 'POST':
            form = AddQuestionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'quiz/add_question.html', context)
    else:
        return redirect('home')


def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('login_user')
        context = {
            'form': form
        }
        return render(request, 'quiz/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        context = {}
        return render(request, 'quiz/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('/')
