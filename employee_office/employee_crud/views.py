from django.shortcuts import render, redirect, get_object_or_404
from .models import EmployeeDetails
from .forms import EmpForm
from django.views.generic import ListView, DetailView

class IndexView(ListView):
    template_name = 'crudapp/index.html'
    context_object_name = 'employee_list'
    
    def get_queryset(self):
        return EmployeeDetails.objects.all()

class EmpDetailView(DetailView):
    model = EmployeeDetails
    template_name = 'crudapp/employee-detail.html'

def create(request):
    if request.method == 'POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = EmpForm()
    return render(request,'crudapp/create.html',{'form': form})

def edit(request, pk, template_name='crudapp/edit.html'):
    employee = get_object_or_404(EmployeeDetails, pk=pk)
    form = EmpForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name ,{'form':form})

def delete(request, pk, template_name='crudapp/confirm_delete.html'):
    employee = get_object_or_404(EmployeeDetails, pk=pk)
    if request.method=='POST':
        employee.delete()
        return redirect('index')
    return render(request, template_name, {'object':employee})

