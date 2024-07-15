from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model,login


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