from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def add_record(request):
    return render(request, 'add_record.html')

def add_record_action(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        symptoms = request.POST['symptoms']
        prescription = request.POST['prescription']
        date = request.POST['date']

        p_obj = Patient()
        p_obj.name = name
        p_obj.age = age
        p_obj.gender = gender
        p_obj.symptoms = symptoms
        p_obj.prescription = prescription
        p_obj.date_of_visit = date
        p_obj.save()
        messages.info(request,"Record added successfully")
        return redirect('show_records')
    else:
        return render(request, 'show_records.html')

def show_records(request):
    data = Patient.objects.all()
    return render(request, 'show_records.html', {'data':data})

def delete_data(request):
    id = request.GET['id']
    Patient.objects.filter(id = id).delete()
    data = Patient.objects.all()
    messages.info(request,"Data deleted successfully")
    return render(request,'show_records.html',{'data':data})