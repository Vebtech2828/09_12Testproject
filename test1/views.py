from django.shortcuts import render
from . import forms
# from django.http import HttpResponse

def fun1(request):
    return render(request, 'result.html')


def fun2(request):
    return render(request, 'Home.html')


def empperforview(request):
    form = forms.DataEmp()
    if request.method=='Register':
        form=forms.DataEmp(request.Register)
        if form.is_valid():
            print('Form Validation Sucess and printing Data')
            print('Name',from.cleared_data['name'])
            print('Performance',form.cleared_data['performance'])
        return render(request,'result.html',{'Form': form})
