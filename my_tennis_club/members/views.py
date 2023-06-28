from email import message
from urllib import request
from django.shortcuts import redirect, render
from .forms import MyRegisterform
from django.contrib import messages
from .models import Registerform
# Create your views here.


def temp(request):
    return render(request,'tem.html')

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


def update(request,id):
    data =Registerform.objects.get(id=id)
    
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        email=request.POST['email']
        
        data.name=name
        data.age=age
        data.address=address
        data.contact=contact
        data.email=email
        data.save()
        messages.success(request,"update successfully completed")
        
        # sometime quotation matters a lot '' or "" if we using single quotation somewhere then used similar to everywhere otherwise same code work twice
        # messages.success(request,'update successfully completed')
        return redirect('Home')
    return render(request,"update.html",{'data':data})

def delete(request,cl):
    data=Registerform.objects.get(id=cl)
    data.delete()
    messages.error(request,"delete successfully completed")
    return redirect('Home') 