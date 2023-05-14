from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from apps.forms import RegisterForm, LoginForm


def register_view(request):
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')
        else:
            print(form.errors)
    return render(request,'account/register.html')



def login_view(request):
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.data.get('username')
            password = forms.data.get('password')
            users = authenticate(username=username, password=password)
            if users:
                login(request, users)
                return redirect('home')
        else:
            print(forms.errors)
    return render(request, 'account/login.html')

def home(request):
    return render(request,'home.html')

