import imp
from urllib import response
from django.shortcuts import render,redirect
from django.http import HttpResponse
from demo3.models import enqmodel
from demo3.forms import enqform
import csv

# Create your views here.
def enqview(request):
    form=enqform()
    if request.method=='POST':
        form=enqform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("data is created")
    return render(request,'enq.html',{'form':form})

def updateenqview(request,pk):
    res=enqmodel.objects.get(id=pk)
    form=enqform(instance=res)
    if request.method=='POST':
        form=enqform(request.POST,instance=res)
        if form.is_valid():
            form.save()
            return redirect('/d3/select/')

    return render(request,'enq.html',{'form':form})

def selectenqview(request):
    res=enqmodel.objects.all()
    return render(request,'d3sel.html',{'res':res})

def deleteenqview(request,pk):
    res=enqmodel.objects.get(id=pk).delete()
    return redirect('/d3/select/')

def download_csv(request):
    res=enqmodel.objects.all()
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;filename=enq.csv'
    csv_writer= csv.writer(response)
    csv_writer.writerow(['name','phone','email','address','desc','date'])
    for i in res:
        csv_writer.writerow([i.name,i.phone,i.email,i.address,i.desc,i.date])
    return response

