from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
def home_view(request):
    return render(request,'home.html')


def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('phone_number')
        p = request.POST.get('password')
        user = authenticate(request, username = u,password = p)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'users/auth.html',{'error':'số điện thoại hoặc mật khẩu sai'})
    return render(request,'users/auth.html') 

def register_view(request):
    if request.method == 'POST':
        n = request.POST.get('full_name')
        u = request.POST.get('phone_number')
        i_c = request.POST.get('identity_card')
        p = request.POST.get('password')
        cp = request.POST.get('confirm_password')
        if User.objects.filter(phone_number = u).exists():
            return render(request,'users/register.html',{'error':'số điện thoại đã được sử dụng'})
        if cp != p :
            return render(request, 'users/register.html',{'error':'mật khẩu không khớp'})
        if len(i_c) != 12:
            return render(request,'users/auth.html',{'error':'phải là 12 chữ số'})
        new_user = User.objects.create_user(
            phone_number = u, 
            password=p,
            identity_card = i_c,
            full_name= n
            )
        return redirect('login')
    return render(request,'users/register.html')       

def logout_view(request):
    logout(request)
    return redirect('login')