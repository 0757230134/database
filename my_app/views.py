from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    return render(request, 'home.html')

def submit(request):
    if request.method == "POST":
        name = request.POST.get('names')
        email = request.POST['email']
        dob = request.POST['dob']
        phone = request.POST['phone']
        print(name, email, dob, phone)
    return redirect('home-page')

