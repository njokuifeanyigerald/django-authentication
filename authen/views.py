from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,get_user_model,login,logout

def home(request):
    form = RegisterForm(request.POST or None)
    # if request.method == 'POST':
    if form.is_valid():
        form.save()
        
        new_user = authenticate(username=username, email=email,password =password)
        login(request, new_user)
        form = RegisterForm(request.POST or None)
        return redirect('login')
    context = {
        "form":form
    }
    return render(request, "home.html", context)

def login(request):
    # next = request.GET.get('next')
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = forms.cleaned_data.get('username')
            password = forms.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request)
            form = RegisterForm(request.POST or None)
            return redirect('login/')
    context = {
        "form":form
    }
    return render(request, "login.html", context)

@login_required
def profile(request):
    return render(request, "profile.html", {})

def logout(request):
    logout(request)
    return redirect('/')