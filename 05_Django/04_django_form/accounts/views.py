from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
# Authentication(인증) -> 신원 확인
#    - 자신이 누구라고 주장하는 사람의 신원을 확인하는 것

def signup(request):
    # 이미 로그인 되어있는 친구가 회원가입 하려고 하면
    if request.user.is_authenticated:
        return redirect('articles:index')


    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)



def login(request):
    # 이미 로그인 되어있는 친구가 로그인 하려고 하면
    if request.user.is_authenticated:
        return redirect('articles:index')


    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')