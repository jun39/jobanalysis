from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Company
from .forms import CompanyForm

def index(request):
    data = Company.objects.all()
    params = {
        'title':'登録した企業情報',
        'message':'全ての登録した企業情報',
        'date':data,
    }
    return render(request,'inputApp/list.html',params)

def create(request):
    params ={
        'title':'企業情報を入力しました',
        'form':CompanyForm(),
    }
    if (request.method == 'POST'):
         company = request.POST['company']
         location = request.POST['location']
         office = request.POST['office']
         establishment = request.POST['establishment']
         capitalStock = request.POST['capitalStock']
         sales = request.POST['sales']
         employees = request.POST['employees']
         averageAge = request.POST['averageAge']
         startingSales = request.POST['startingSales']
         workingHours = request.POST['workingHours']
         company = Company(company=company,location=location,office=office,establishment=establishment,capitalStock=capitalStock,sales=sales,employees=employees,averageAge=averageAge,startingSales=startingSales,workingHours=workingHours)
         company.save()
         return redirect(to='/inputApp')
    return render(request,'inputApp/create.html', params)
