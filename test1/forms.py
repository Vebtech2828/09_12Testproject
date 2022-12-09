from django import forms

class DataEmp(forms.Form):
    empname = forms.CharField(max_length=30)
    empperfor = forms.IntegerField()