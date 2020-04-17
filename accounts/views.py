from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse
from .forms import CompanyForm

def index(request):
    params = {
          'title':'企業の情報を入力してください',
          'form':CompanyForm()
      }
    if(request.method == 'POST'):
        params['form'] = CompanyForm(request.POST)
    return render(request, 'accounts/login.html',params)

# def form(request):
#     company = request.POST['company']
#     params ={
#         'company': company + '社を登録しました',
#     }
#     return render(request, 'accounts/create.html',params)