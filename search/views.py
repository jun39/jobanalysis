from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.paginator import Paginator
def index(request):
    params = {
        'title':'マイページ',
        'message':'登録してください',
    }
    return render(request,'search/mypage.html',params)
