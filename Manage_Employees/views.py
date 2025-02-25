from django.shortcuts import render,redirect
from .models import *


# Create your views here.

def manage_employees(request):
    total_employees = Employee.objects.count()
    emp = Employee.objects.all()
    contaxt = {'emp': emp
                ,'total_employees': total_employees}
    return render(request, 'index.html',contaxt)


def add_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        emp = Employee(name=name, email=email, address=address, phone=phone)
        emp.save()
        return redirect('home')
    return render(request, 'index.html')


def edit_employee(request, id):
    emp = Employee.objects.all()
    contaxt = {'emp': emp}
    return render(request, 'index.html', contaxt)


def update_employee(request, id):
    emp = Employee.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        emp = Employee(id =id,name=name, email=email, address=address, phone=phone)
        emp.save()
        return redirect('home')
    return render(request, 'index.html')


def delete_employee(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('home')



def delete_all(request):
    emp = Employee.objects.all()
    emp.delete()
    return redirect('home')
