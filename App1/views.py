from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def func(request):
    return HttpResponse('We are in func1')

def fun2(request,name):
    return HttpResponse(f'My name is {name}')

def fun3(request):
    a=int(request.GET.get('n1'))
    b=int(request.GET.get('n2'))
    return HttpResponse(f'The sum of 2 nums is {a+b}')

# def home(request):
#     d={'name':'divya'}
#     return render(request,'../Templates/index.html',d)

def students(request):
    listofstudents=[['divya','CSE',523],['maya','CSE',552],['Navya','EEE',322]]
    context={'data':listofstudents}
    return render(request,'../Templates/home.html',context)
    