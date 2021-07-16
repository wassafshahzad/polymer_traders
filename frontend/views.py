from django.shortcuts import render

# Create your views here.


def sign_up(request):
    return render(request, "frontend/SignUpPage.html")


def welcome_page(request):
    return render(request, "frontend/Welcome.html")
