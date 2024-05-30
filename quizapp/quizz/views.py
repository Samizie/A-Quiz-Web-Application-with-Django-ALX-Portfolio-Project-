from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import  HttpResponse



# Create your views here.
'''
def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions = QuizModel.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            answer = 
            if q.ans == request.POST.get(q.question):
                score += 1
                correct += 1
            else:
                wrong +=1
        percent = (score/total) * 100
        context = {
            'score':score,
            'time':request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total,
        }
        return render(request, "Quiz/result.html", context)
    else:
        questions = QuizModel.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'Quiz/home.html', context)'''

def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions = QuizModel.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            print(request.POST.get(q.question))
            print(q.ans)
            #print()
            answer = request.POST.get(q.question)
            if q.ans == answer:
                score += 1
                correct += 1
            else:
                wrong +=1
        percent = round((score/total) * 100, 2)
        context = {
            'score':score,
            'time':request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total,
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
        form = AddQuestionsForm()
        if(request.method=='POST'):
            form=AddQuestionsForm(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={
            'form':form,
            }
        return render(request, 'Quiz/addquestion.html', context)
    else:
        return redirect ('home')
    
def register(request):
    if request.user.is_authenticated:
        return redirect ('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('/')
        context={
            'form':form,
            }
        return render (request, 'Quiz/register.html', context)

    

        
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method =="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect ('/')
        context={}
        return render(request, 'Quiz/login.html', context)
        
def logoutPage(request):
    logout(request)
    return redirect('/')


