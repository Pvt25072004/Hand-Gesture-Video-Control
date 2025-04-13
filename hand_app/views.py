from django.shortcuts import render

def base(request):
    return render(request, 'hand_app/base.html')
def home(request):
    return render(request, 'hand_app/home.html')
def index(request):
    return render(request, 'hand_app/index.html')
def login(request):
    return render(request, 'hand_app/login.html')
def register(request):
    return render(request, 'hand_app/register.html')
def about(request):
    return render(request, 'hand_app/about.html')
