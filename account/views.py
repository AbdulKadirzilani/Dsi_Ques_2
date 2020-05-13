
from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth import authenticate, login
from .forms import loginForm
from django.http import HttpResponse
from .models import Information

def loginView(request):

            forms = loginForm(request.GET or None)

            email= request.GET.get('email', None)
            password = request.GET.get('password', None)

            print(email)
            print(password)
            if email and password:
                    students = Information.objects.filter(email = email).filter(password__contains =  password)
                    print(students)

                    if students:
                        return render(request, 'thankyou.html')
                    else:
                        return HttpResponse("Username or password incorrect")


            context = {'forms': forms}
            return render(request, 'loginView.html', context)