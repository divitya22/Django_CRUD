from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
from django.http import HttpResponseRedirect




def home(request):
    return render(request,"home.html")


def detail(request):
    emp_list=Employee.objects.all()
    return render(request,"index.html",{"emp_list":emp_list})



def add_data(request):
    submitted=False
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_data?submitted=True')
    else:
        form=EmployeeForm
        if 'submitted' in request.GET:
            submitted=True


    return render(request,"forms.html",{"form":form,"submitted":submitted})



def list_emp(request):
    lis_emp=Employee.objects.all()
    return render(request,"list_emp.html",{"lis_emp":lis_emp})


def show_emp(request,emp_id):
    emp=Employee.objects.get(pk=emp_id)
    return render(request,"show_emp.html",{"emp":emp})


def delete_emp(request,emp_id):
    emps=Employee.objects.get(pk=emp_id)
    emps.delete()
    return redirect('list-emp')


def update_emp(request,emp_id):
    emp=Employee.objects.get(pk=emp_id)
    form=EmployeeForm(request.POST or None,instance=emp)
    if form.is_valid():
        form.save()
        return redirect('list-emp')

    return render(request,"update_emp.html",{"emp":emp,"form":form})

