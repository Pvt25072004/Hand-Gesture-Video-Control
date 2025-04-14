from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def base(request):
    return render(request, 'hand_app/base.html')

def home(request):
    return render(request, 'hand_app/home.html')

def index(request):
    return render(request, 'hand_app/index.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)
            messages.success(request, "Đăng nhập thành công")
            return redirect('index')
        else:
            messages.error(request, "Tài khoản hoặc mật khẩu không đúng")

    return render(request, 'hand_app/login.html')

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Đăng ký thành công! Hãy đăng nhập.")
            return redirect('login')
        else:
            messages.error(request, "Đăng ký thất bại. Vui lòng thử lại.")
            print(form.errors)
    else:
        form = UserCreationForm()

    return render(request, 'hand_app/register.html', {'form': form})

def about(request):
    return render(request, 'hand_app/about.html')
