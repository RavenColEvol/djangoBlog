from django.shortcuts import render,redirect
from .models import BlogPosts
from .forms import BlogForms,UserName
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    blogs = BlogPosts.objects.all()
    return render(request,'home/index.html',{'blogs':blogs})

def detail(request,id):
    blogs = BlogPosts.objects.get(id=id)
    return render(request,'home/details.html',{'blogs':blogs})

def addPost(request):
    form = BlogForms()
    if request.method == "POST":
        form = BlogForms(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    return render(request,'home/forms.html',{'form':form})

def addUser(request):
    form = UserName()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'authentication/login.html',{'form':form})

def UserAuth(request):
        form = UserName()
        context = {'form':form}
        if request.method == "POST":
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request,username=username,password=password)
                if user:
                        login(request,user)
                        return redirect('/')
                else:
                        context['error']='Invalid Login Cerdential'
                        return render(request,'authentication/signin.html',context)
        else:
                return render(request,'authentication/signin.html',context)

def userlogout(request):
        logout(request)
        return redirect('/')