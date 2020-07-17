from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm  # 로그인에 사용하는 form
from django.contrib.auth import login, authenticate, logout
# Create your views here.

def login_view(request):    # 함수형으로 view 작성
    if request.method == "POST":
        form = LoginForm(request=request,data=request.POST) # 왜 하나는 걍 request, 하나는 request.POST ?
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("list") # 유저가 아니면 다시 list.html로 돌아가!

    else :  # else ?
        form = LoginForm() # -> 빈 상태
        return render(request, "account.html",{"form":form})

def logout_view(request):
    logout(request)
    return redirect("login")    # logout을 하면 'login' 페이지로 넘어간다!

def register_view(request):   
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)    # 회원가입 하자마자 로그인 된 상태로 만들어준다 # 근데 이게 왜 ? 어떻게 만들어주는 거지?
            return redirect("list")
        return render(request, "account.html",{"form":form})
            
    else :
        form = RegisterForm() # -> 빈 상태
        return render(request, "account.html",{"form":form})