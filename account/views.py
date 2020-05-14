
# Create all Query for LoginView

from django.shortcuts import render
from .forms import loginForm
from django.http import HttpResponse
from .models import DatabaseField

def loginView(request):

            forms = loginForm(request.GET or None)

            email= request.GET.get('email', None)
            password = request.GET.get('password', None)

            print(email)
            print(password)
            if email and password:
                    students = DatabaseField.objects.filter(email = email).filter(password__contains =  password)
                    print(students)

                    if students:
                        return HttpResponse("Sucessfully Login")
                    else:
                        return HttpResponse("Email or password incorrect")


            context = {'forms': forms}
            return render(request, 'loginView.html', context)