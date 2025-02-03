from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

def func_template(requset):
    return render(requset, 'func_template.html')

