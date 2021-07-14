from django.shortcuts import redirect, render

# Create your views here.


def sign_up(request):
    return render(request, 'frontend/SignUpPage.html')


def welcome_page(request):
    if not request.user:
        return redirect('signup')
    else:
        return render(request, 'frontend/Welcome.html', {
            'user_name', request.user.user_name})
