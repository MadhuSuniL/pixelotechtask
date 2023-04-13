from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def signup(request):
    return render(request, 'signup.html')
def login(request):
    return render(request, 'signin.html')

def home(request):
    
    print(request.user.username)
    
    if request.user.username == 'AnonymousUser' or request.user.username == '':
        return render(request, 'signin.html')
    
    return render(request, 'home.html')
