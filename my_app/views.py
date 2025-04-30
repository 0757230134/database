from itertools import count
from tkinter.font import names

from django.shortcuts import render, redirect

from my_app.models import Person


# Create your views here.

def home(request):
    return render(request, 'home.html')

def submit(request):
    if request.method == "POST":
        name = request.POST.get('names')
        email = request.POST['email']
        dob = request.POST['dob']
        phone = request.POST['phone']
        weight = request.POST['weight']
        height = request.POST['height']
        gender = request.POST['gender']
        print(name, email, dob, phone, weight ,height, gender)
        Person.objects.create(name=name, email=email, dob=dob, phone=phone,weight=weight, height=height, gender=gender)
        count = Person.objects.all().count()
        print(f"You have {count} records")
    return redirect('home-page')

def people(request):
    data = Person.objects.all()
    return render(request,'list.html',{'data':data})
def details(request,id):
    person = Person.objects.get(id=id)
    return render(request,'details.html',{'person':person})
