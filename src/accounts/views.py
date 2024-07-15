from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model,login,logout,authenticate


User = get_user_model()

# Create your views here.
def SignUp(request):

    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        user = User.objects.create_user(username=Username, password=Password)
        login(request,user)
        return redirect('page_acceuil_boutique')

    return render(request, 'SignUp.html')


def LogIn_user(request):
    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        user = authenticate(request, username=Username, password=Password)
        if user is not None:
            login(request, user)
            return redirect('page_acceuil_boutique')
        
    return render(request, 'Login.html')


def LogOut_user(request):
    logout(request)
    return redirect('page_acceuil_boutique')