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
        'form':CompanyForm(),
        'data':[],
    }
    if (request.method == 'POST'):
        num = request.POST['id']
        n = request.POST['name']
        item = Company.objects.get(id = num,company=n)
        params['data'] = [item]
        params['form'] = CompanyForm(request.POST)
    else:
        params['data'] = Company.objects.all()
    return render(request,'inputApp/list.html',params)

def create(request):
    if (request.method == 'POST'):
         obj = Company()
         company = CompanyForm(request.POST,instance=obj)
         company.save()
         return redirect(to='/inputApp')
    params ={
        'title':'企業情報を入力しました',
        'form':CompanyForm(),
    }
    return render(request,'inputApp/create.html', params)

def edit(request,num):
    obj = Company.objects.get(id=num)
    if(request.method=='POST'):
        company =CompanyForm(request.POST,instance=obj)
        company.save()
        return redirect(to='/inputApp')
    params ={
        'title':'企業情報を編集してください',
        'id':num,
        'form':CompanyForm(instance=obj),
    }
    return render(request,'inputApp/edit.html',params)