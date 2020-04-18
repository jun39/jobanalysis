from django import forms
from .models import Company,Comment
class FindForm(forms.Form):
     find = forms.CharField(label='検索フォーム',required=False)


class CompanyForm(forms.ModelForm):
     class Meta:
         model = Company
         fields = ['company','location','office','establishment','capitalStock','sales','employees','averageAge','startingSales','workingHours']


class CommentForm(forms.ModelForm):
     class Meta:
          model = Comment
          fields = ['company','title','content']