from django import forms

class CompanyForm(forms.Form):
     id = forms.IntegerField(label='ID')
     name = forms.CharField(label='会社名')