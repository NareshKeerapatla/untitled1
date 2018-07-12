from django.shortcuts import render

from django.http import HttpResponse
from .models import Reg
from .forms import LoginForm,RegForm
def reg(request):
    if request.method=='POST':
        form=RegForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse('success')
        else:
            print(form.errors)
            return HttpResponse('error')
    else:
        form=RegForm()
        return render(request,'reg.html',{'form':form})
def login(request):
    if request.method=="POST":
        mylogin=LoginForm(request.POST)
        if mylogin.is_valid():
            U=mylogin.cleaned_data['User']
            P=mylogin.cleaned_data['Pwd']
            db=Reg.objects.filter(User=U,Pwd=P)
            if not db:
                return HttpResponse('login failed')
            else:
                return HttpResponse('login success')
    else:
        form=LoginForm()
        return render(request,'login.html',{'form':form})
def home(request):
    return render(request,'home.html')
