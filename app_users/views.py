from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from app_users.forms import AuthForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from app_users.forms import RegisterForm
from app_users.models import Profile

class AnotherLoginView(LoginView):
    template_name = 'users/login.html'

class NewLoginView(View):
    def get(self,request):
        auth_form = AuthForm()
        context = {
            'form': auth_form
        }
        return render(request,'users/login.html',context=context)

    def post(self,request):
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username = username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Вы успешно вошли в систему')
                else:
                    auth_form.add_error('__all__','Ошибка! Учетная запись пользователя не активна')
            else:
                auth_form.add_error('__all__','Ошибка! проверьте введеные данные')


class NewLogoutView(LogoutView):
    next_page = '/'


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request,'users/register.html',{'form':form})

def another_register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            date_of_birth =form.cleaned_data.get('date_of_birth')
            city = form.cleaned_data.get('city')
            Profile.objects.create(
                user = user,
                city = city,
                date_of_birth = date_of_birth
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request,'users/register.html',{'form':form})

# Create your views here.
