from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from curd_op.forms import EmployeeForm
from curd_op.models import Employee

# Create your views here.
def emp(request):
	form = EmployeeForm(data=request.POST)
	if request.method == "POST":
		
		if form.is_valid():
			try:
				form.save()
				return redirect('/show')
			except:
				pass
		else:
			form = EmployeeForm()
	return render(request,'index.html',{'form':form})

def show(request):
	employees = Employee.objects.all()
	return render(request,"show.html",{'employee':employees})


def edit(request, id):
	employee = Employee.objects.get(id=id)
	return render(request,'edit.html', {'employee':employee})

def update(request, id):
	employee = Employee.objects.get(id=id)
	form = EmployeeForm(data=request.POST, instance = employee)
	if form.is_valid():
		form.save()
		return redirect("/show")
	return render(request, 'edit.html', {'employee': employee})


def destroy(request, id):
	employee = Employee.objects.get(id=id)
	employee.delete()
	return redirect("/show")
