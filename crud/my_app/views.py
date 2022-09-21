from django.shortcuts import render,redirect
from .models import Employee

# Create your views here.
def index(request):
    emp = Employee.objects.all()
    return render(request,'index.html',{'employee':emp})


def form(request):
    if request.method == 'POST':
        user_name = request.POST['name']
        user_address = request.POST['address']
        user_deppt = request.POST['deppartment']
        emp = Employee(name=user_name,address=user_address,deppt=user_deppt)
        emp.save()
        return redirect('/')
    else:
        return render(request,'form.html')

def update(request,pk):
    emp = Employee.objects.get(id=pk)
    return render(request,'update.html',{'employee':emp})

def update_detail(request,pk):
    user_name = request.POST['name']
    user_address = request.POST['address']
    user_deppt = request.POST['deppartment']
    emp = Employee.objects.get(id=pk)
    emp.name = user_name
    emp.address = user_address
    emp.deppt = user_deppt
    emp.save()
    return redirect('/')

def delete(request,pk):
    emp = Employee.objects.get(id=pk)
    emp.delete()
    return redirect('/')
    

