from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'UserName Taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email Taken')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()
                print('User Created')
        else:
            messages.info(request, 'Password mismatch')
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")
