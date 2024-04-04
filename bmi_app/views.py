from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required

# Create your views here.
def HomePage(request):
    return render(request, 'home.html')

@login_required(login_url = 'login')
def calculate_bmi(request):
    if request.method == 'POST':
        height = float(request.POST['height'])
        weight = float(request.POST['weight'])
        bmi = weight / (height ** 2)
        category = ''
        if bmi < 18.5:
            category = 'Under Weight'
        elif 18.5 < bmi < 25:
            category = 'Normal Weight'
        elif 25 < bmi < 30:
            category = 'Over Weight'
        elif 30 < bmi < 35:
            category = 'Obessity'
        else :
            category = 'Extreme Obessity'
        context = {'bmi': round(bmi, 2), 'category': category}
        return render(request, 'outcome.html', context)
    return render(request, 'calculate.html')

def SignupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return HttpResponse("Your password and confirm password are not same.")
        else:
            my_user = User.objects.create_user(username,email,password1)
            my_user.save()
            return redirect('login') 
    return render(request, 'signup.html')    

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        passsword=request.POST.get('password')  
        user=authenticate(request, username=username,password=passsword)
        if user is not None:
            login(request,user)
            bmi_user=user.username
            return render(request,"calculate.html",{'username':bmi_user})
        else:
            return HttpResponse("Wrong Informations!!!")
            return redirect('home') 

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


