from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import ContactMessage

# Create your views here.

# Create your views here.
def projecthomepage(request):
    return render(request,'projecthomepage.html')
def aboutus(request):
    return render(request,'aboutus.html')
from django.shortcuts import  render
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request, 'signup.html')
def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'projecthomepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')


def signup1(request):
    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['password']
        pass2=request.POST['password1']
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Username already taken')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfully!!')
                return render(request,'login.html')
        else:
            messages.info(request,'Password do not match')
            return render(request,'signup.html')
def logout(request):
    auth.logout(request)
    return render(request,'login.html')
def donate(request):
    return render(request,'donate.html')
def urgent(request):
    return render(request, 'urgent.html')
def animals(request):
    return render(request,'animals.html')
def children(request):
    return render(request,'children.html')
def hungry(request):
    return render(request,'hungry.html')
def disability(request):
    return render(request,'disability.html')
def medical(request):
    return render(request,'medical.html')
def education(request):
    return render(request,'education.html')
def women(request):
    return render(request,'women.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Create a new ContactMessage object and save it to the database
        ContactMessage.objects.create(name=name, email=email, message=message)

        # Optionally, you can add a success message here
        messages.success(request, 'Message sent successfully!')

        # Redirect the user to the homepage or any other page after successful submission
        return redirect('projecthomepage')  # Change 'projecthomepage' to the correct URL name for your homepage
    else:
        return render(request, 'contact.html')
def gallery(request):
    return render(request,'gallery.html')
from django.http import JsonResponse


