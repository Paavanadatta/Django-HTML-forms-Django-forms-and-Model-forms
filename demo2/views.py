from django.shortcuts import render
from django.http import HttpResponse
from demo2.forms import registerform
from demo2.models import regmodel

# Create your views here.
def registerview(request):
    form=registerform()
    if request.method=='POST':
       form=registerform(request.POST)
       if form.is_valid():
            print(form)
            regmodel.objects.create(username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email'],
            phone=form.cleaned_data['phone'])
            return HttpResponse("record is created")
    return render(request,'reg.html',{ 'form':form })

def updateview(request,pk):
    res=regmodel.objects.get(id=pk)
    if request.method=='POST':
       form=registerform(request.POST)
       if form.is_valid():
            print(form)
            regmodel.objects.filter(id=pk).update(username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email'],
            phone=form.cleaned_data['phone'])
            return HttpResponse("record is updated")
    return render(request,'upd.html',{ 'i':res })
   

def selectview(request):
    res=regmodel.objects.all()
    return render(request,'sel.html',{'res':res})

def deleteview(request,pk):
    res=regmodel.objects.get(id=pk).delete()
    return HttpResponse(" Record is deleted")