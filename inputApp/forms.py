from django import forms
from .models import Company
class SearchForm(forms.Form):
     id = forms.IntegerField(label='ID')
     name = forms.CharField(label='会社名')

class CompanyForm(forms.ModelForm):
     class Meta:
         model = Company
         fields = ['company','location','office','establishment','capitalStock','sales','employees','averageAge','startingSales','workingHours']