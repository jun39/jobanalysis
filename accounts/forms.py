from django import forms

class CompanyForm(forms.Form):
     company = forms.CharField(label='company')
     location = forms.CharField(label='location')
     office = forms.CharField(label='office')
     establishment = forms.IntegerField(label='establishment')
     capitalStock = forms.IntegerField(label='capitalStock')
     sales = forms.IntegerField(label='sales')
     employees = forms.IntegerField(label='employees')
     averageAge = forms.IntegerField(label='averageAge')
     startingSales = forms.IntegerField(label='startingSales')
     workingHours = forms.IntegerField(label='workingHours')
