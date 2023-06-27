from django.shortcuts import redirect, render
from .forms import MyRegisterform
from django.contrib import messages
from .models import Registerform
# Create your views here.


def home(request):
    data = Registerform.objects.all()
    if (data!=''):
        return render(request,"home.html",{'data':data})
    else:    
       return render(request,'home.html')
    
def insert(request):
    if request.method=='POST':
        form = MyRegisterform(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,"Registration successfully completed")
                return redirect("Home")
            except:
                pass
    else:
       form = MyRegisterform()
    return render(request,'register.html',{'form':form})    