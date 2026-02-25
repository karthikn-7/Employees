from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .form import EmployeeForm


def employee_list(request):
    # print("--------------------")
    # print(dir(request))
    # print("--------------------")
    
    employees = Employee.objects.all()
    return render(request,"employees/list.html",{"employees":employees})


def get_employee_detail(request, id):
    
    employee = get_object_or_404(Employee, id=id)
    return render(request,"employees/detail.html",{"employee":employee})


def employee_create(request):
    
    if(request.method == "POST"):
        # print(type(request.POST['joined_date']))
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
            
    return render(request, "employees/create.html", {"form": form})

def employee_update(request, id):
    employee = get_object_or_404(Employee,id=id)
    if(request.method == "POST"):
        # print(type(request.POST))
        print("-----------::: ", request.POST)
        name = request.POST["name"]
        email = request.POST["email"]
        department = request.POST["department"]
        joined_date = request.POST["joined_date"]
        # print(name, email, department, joined_date)
        
        
        employee.name = name
        employee.department = department
        employee.email = email
        if joined_date:
            employee.joined_date = joined_date
        employee.save()
        
        return redirect("employee_list")
    
    return render(request, 'employees/update.html',{"employee":employee})



# microservices

