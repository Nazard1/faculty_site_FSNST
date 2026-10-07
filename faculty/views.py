from django.shortcuts import render, get_object_or_404
from .models import Department, Program, Subject, Teacher, HomePage, ExchangeProgram

def homepage(request):
    page = HomePage.objects.first()
    return render(request, 'faculty/homepage.html', {'homepage': page})

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'faculty/department_list.html', {'departments': departments})

def department_detail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'faculty/department_detail.html', {'department': department})

def program_list(request):
    programs = Program.objects.all()
    return render(request, 'faculty/program_list.html', {'programs': programs})

def program_detail(request, pk):
    program = get_object_or_404(Program, pk=pk)
    return render(request, 'faculty/program_detail.html', {'program': program})

def exchange_list(request):
    exchange_programs = ExchangeProgram.objects.order_by('deadline')
    return render(request, 'faculty/exchange_list.html', {'exchange_programs': exchange_programs})   