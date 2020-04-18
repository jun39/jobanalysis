from django import forms
from .models import Company
class FindForm(forms.Form):
     find = forms.CharField(label='検索フォーム',required=False)

class CompanyForm(forms.ModelForm):
     class Meta:
         model = Company
         fields = ['company','location','office','establishment','capitalStock','sales','employees','averageAge','startingSales','workingHours']