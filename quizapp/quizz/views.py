from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import  HttpResponse



# Create your views here.
def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions = QuizModel.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.question):
                score += 10
                correct += 1
            else:
                wrong +=1
        percent = score/(total*10) * 100
        context = {
            'score':score,
            'time':request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        return render(request, "Quiz/result.html", context)
    else:
        questions = QuizModel.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'Quiz/home.html', context)
    
def add_ques(request):
    if request.user.is_staff:
        return redirect("/home")
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm()(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect("/login")
            context = {
                'from' : form,
            }
            return render(request, 'Quiz/register.html', context)
        
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method =="POST":
            username=request.POST.get('username')
            password=password.POST.get('password')
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request.user)
                return redirect ('/')
            context={}
            return render(request, 'Quiz/login.html', context)
        
def logout(request):
    logout(request)
    return redirect('/')


