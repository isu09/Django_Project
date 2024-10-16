from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        user_name = request.POST['NAME']
        password = request.POST['PASSWORD']
        user = auth.authenticate(username = user_name, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"user doesn't exist")
            return redirect('login')
    else:
         return render(request,"login.html")



def register(request):
    if request.method == 'POST':
        user_name = request.POST['NAME']
        password1 = request.POST['PASSWORD1']
        password2 = request.POST['PASSWORD2']
        if password1 == password2:
            if User.objects.filter(username= user_name).exists():
                messages.info(request,"user exist")
                print("user name exist")
                return redirect("register")
            else:
                user = User.objects.create_user(username = user_name, password = password1 )
                user.save()
                messages.info(request,"user created")
                print("user created")
                return redirect("login")
            
            
        else:
            messages.info(request,"user not created")
            print("user not created")
            return redirect("register")

        
        
        return redirect("/")

    else:
        return render(request,"register.html")


