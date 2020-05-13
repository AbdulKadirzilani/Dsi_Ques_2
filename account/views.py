
from django.shortcuts import render,HttpResponse, Http404, get_object_or_404, redirect
#from .models import author, category, article, comment
from django.contrib.auth import authenticate, login, logout
from .forms import loginForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .models import Information

def search_student(request):
    print("ok")
    forms = loginForm(request.GET or None)

    roll= request.GET.get('email', None)
    semester = request.GET.get('password', None)
    print(roll)
    print(semester)
    if roll and semester:
        students = Information.objects.filter(email = roll).filter(password__contains =  semester)
        print(students)

        #if roll:
            #students = students.filter(roll=roll)
        #if session:
           # students = students.filter(session=session)


        context = {'forms': forms, 'students': students}
        return render(request, 'search_result.html', context)

    context = {'forms': forms}
    return render(request, 'search_result.html', context)


def user_login(request):

  if request.user.is_authenticated:
        return render(request, 'thankyou.html')
  else:
    if request.method == 'POST':
        username = request.POST.get('users')
        password = request.POST.get('pass')
        user2 = authenticate(request, username=username, password=password)
        if user2:
        #user is not None:
            login(request, user2) #user2 ta sucessful hole login korbo
            return render(request, 'thankyou.html') #login hole ekta page e niya jabe
        else:
            return HttpResponse("Username or password incorrect")
    return render(request, 'log1/login.html')



def user_logout(request):
    logout(request)
    return redirect('login')
    #return render(request, 'log1/thankyou2.html')
    #return HttpResponseRedirect(login.get_absolute_url())


# def getRegister(request):
#     form = RegisterForms(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.is_active = False
#         instance.save()
#         site=get_current_site(request)
#         mail_subject="Confirmation message for blog"
#         message=render_to_string('confirm_email.html',{
#             "user":instance,
#             'domain':site.domain,
#             'uid':instance.id,
#             'token':activation_token.make_token(instance)
#         })
#         to_email=form.cleaned_data.get('email')
#         to_list=[to_email]
#         from_email=settings.EMAIL_HOST_USER
#         send_mail(mail_subject, message, from_email, to_list, fail_silently=True)
#         return HttpResponse("<h1>Thanks for your registration. A confirmation link was sent to your email</h1>")
#     return render(request, 'register.html', {"form": form})

def getRegister(request):
        # if request.method == 'GET':
        #     return render(request, 'register.html')
        if request.method == 'POST':
            form = RegisterForms(request.POST)
            # print(form.errors.as_data())
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('confirm_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    #'uid': urlsafe_base64_encode(force_bytes(user.id)).decode(),
                    'uid': user.id,
                    'token': account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                return HttpResponse('Please confirm your email address to complete the registration')
        else:
            form = RegisterForms
        return render(request, 'register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')



