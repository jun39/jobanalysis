from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import CompanyForm


class CompanyView(TemplateView):
    def __init__(self):
        self.params ={
            'title':'企業の情報を入力してください',
            'form':CompanyForm()
        }
    def get(self,request):
        return render(request,'inputApp/list.html',self.params)
    def post(self,request):
        self.params['form'] = CompanyForm(request.POST)
        return render(request, 'inputApp/create.html',self.params)



