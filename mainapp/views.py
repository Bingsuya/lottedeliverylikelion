from django.shortcuts import render,redirect
from mypageapp.models import User
from django.contrib import auth

# Create your views here.

def main(request):
    return render(request,"main.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['userId']
        password = request.POST['userPwd']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else :
            return render(request, 'login.html', {'error' : '아이디나 비밀번호가 틀렸습니다.'})

    return render(request,'login.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['repassword']:
            user = User.objects.create_user(
                username=request.POST['id'], 
                password=request.POST['password'],
                name=request.POST['name'],
                phone=request.POST['number'],
                address=request.POST['address'],
                )
            return redirect('login')
    return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
