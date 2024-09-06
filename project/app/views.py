from django.shortcuts import render
from django.shortcuts import render
from .form import *
from .models import *

# Create your views here.
def home(request):
    form = ItemInfoForm()
    msg = "Student Registration Page"
    if request.method=='POST':
        form = ItemInfoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            msg = "Registration succsessfully"
        else:
            msg = "Please enter proper data"

    return render(request,'home.html',{'form':form,'msg':msg})

def showdata(request):
    data1 = ItemInfo.objects.all()
    data = data1.values()
    return render(request,'show.html',{'data':data})
