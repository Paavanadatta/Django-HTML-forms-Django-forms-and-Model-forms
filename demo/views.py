from django.shortcuts import render
from django.http import HttpResponse
from demo.models import registermodel

# Create your views here.
def register(request):
    if request.method=='POST':
        print(request.POST)
        user=request.POST['username']
        pas=request.POST['password']
        email=request.POST['email']
        phone=request.POST['phone']
        registermodel.objects.create(username=user,password=pas,email=email,phone=phone)
        return HttpResponse("record is created")
    return render(request,'register.html')

def update(request,pk):
    res=registermodel.objects.get(id=pk)
    if request.method=='POST':
        print(request.POST)
        user=request.POST['username']
        pas=request.POST['password']
        email=request.POST['email']
        phone=request.POST['phone']
        registermodel.objects.filter(id=pk).update(username=user,password=pas,email=email,phone=phone)
        return HttpResponse("record is updated")
    return render(request,'update.html',{'i':res})

def select(request):
    res=registermodel.objects.all()
    return render(request,'select.html',{'res':res})

def delete(request,pk):
    res=registermodel.objects.get(id=pk).delete()
    return HttpResponse(" Record is deleted")