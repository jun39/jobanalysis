from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Company
from .forms import CompanyForm
from .forms import FindForm
def index(request):
    params = {
        'title':'登録した企業情報',
        'message':'全ての登録した企業情報',
        'form':FindForm(),
        'data':[],
    }
    if (request.method == 'POST'):
        num = request.POST['id']
        na = request.POST['name']
        item = Company.objects.get(id = num,company=na)
        params['data'] = [item]
        params['form'] = FindForm(request.POST)
    else:
        params['data'] = Company.objects.all().order_by('sales').reverse()
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

def delete(request,num):
    company = Company.objects.get(id=num)
    if(request.method == 'POST'):
        company.delete()
        return redirect(to='/inputApp')
    params = {
       'title':'選択した企業情報',
       'id':num,
       'obj':company,
    }
    return render(request,'inputApp/delete.html',params)

def find(request):
    if(request.method == 'POST'):
        msg = '検索結果'
        form = FindForm(request.POST)
        str = request.POST['find']
        # リクエストされらformで指定したfind項目の値を取得している
        data = Company.objects.all()[0:int(str)]
    else:
        msg = '企業情報'
        form = FindForm()
        data = Company.objects.all()
    params ={
        'title':'検索項目を入力してください',
        'message':msg,
        'form':form,
        'data':data,
    }
    return render(request,'inputApp/find.html',params)