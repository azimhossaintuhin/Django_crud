from django.shortcuts import render,redirect
from .models import employe

# Create your views here.

def empolyelist(request):
    emp = employe.objects.all()
    contex = {
        'emp':emp
    }
    return render(request,'index.html',contex)


def add(request):
    if request.method=="POST":
        name = request.POST.get('fname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        number = request.POST.get('phone')

        emp = employe(
            NAME = name,
            EMAIL = email,
            ADDRESS = address,
            NUMBER = number
        )
        emp.save()
        return redirect('home')


    return render(request,'index.html')



def edit(request):

    emp = employe.objects.all()
    contex = {
        'emp':emp
    }

    return render(request,'index.html',contex)

def update(request,id):
    if request.method=="POST":
        name = request.POST.get('fname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        number = request.POST.get('phone')

        emp = employe(
            id= id,
            NAME = name,
            EMAIL = email,
            ADDRESS = address,
            NUMBER = number,
            
        )
        emp.save()
        return redirect('home')


    return redirect(request,'index.html')


def delete(request,id):
    emp = employe.objects.filter(id=id)
    emp.delete()
    contex={
        'emp':emp
    }

    return redirect('home')