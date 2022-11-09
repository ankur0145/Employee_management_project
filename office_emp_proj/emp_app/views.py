from django.shortcuts import render, HttpResponse
from . models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'view_all_emp.html',context)

def add_emp(request):
    if request.method =="POST":
        first_name= request.POST['first_name']
        last_name = request.POST['last_name']
        Salary = int(request.POST['Salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['Phone'])
        dept = int(request.POST['dept'])
        Role = int(request.POST['Role'])
        new_emp = Employee=('first_name=first_name, last_name=last_name,Salary=Salary,bonus=bonus,Phone=Phone,dept_id=dept,Role_id=Role,hire_date=datetime.now()')
        new_emp.__str__()
        return HttpResponse('Employee added successfully')
    elif request.method =="GET":
        return render(request, 'add_emp.html')
    else:
        return HttpResponse('An Exception occur:Employee has not added')

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee removed successfully")
        except:
            return HttpResponse("please enter valid EMP id")
    emps=Employee.objects.all()
    context={
        'emps': emps
    }
    return render(request, 'remove_emp.html',context)

def filter_emp(request):
    if request.method=="POST":
        name=request.POST['name']
        Role = request.POST['Role']
        dept = request.POST['dept']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name)| Q(last_name__icontains=name))
        if Role:
            emps=emps.filter(Role__name__icontains=Role)
        if dept:
            emps = emps.filter(dept__name__icontains=dept)

            context={
                'emps':emps

            }
            return render(request,'view_all_emp.html',context)
    elif request.method=="GET":

       return render(request, 'filter_emp.html')

    else:
        return HttpResponse('an Exception occured')