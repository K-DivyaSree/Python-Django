from django.shortcuts import render
from django.http import HttpResponse
from App1.models import *
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
    # listofstudents=[['divya','CSE',523],['maya','CSE',552],['Navya','EEE',322]] - using lists
    listofstudents=[
        {'Name':'Divya', 'Branch':'CSE', 'RollNo':523},
        {'Name':'Maya', 'Branch':'CSE', 'RollNo':595},
        {'Name':'Navya', 'Branch':'EEE', 'RollNo':322},
        {'Name':'Sree', 'Branch':'MECH', 'RollNo':222},
    ]
    context={'data':listofstudents}
    return render(request,'../Templates/home.html',context)
    


def fun(request):
    if request.method=="POST":
        a=request.POST.get('n1')
        d={
            'w': float(int(a)*9.5/100),
        }
        return render(request,'home.html',d)
    return render(request,'home.html')

def cars(request):
    
    if request.method=="POST":
        brand=request.POST.get('carname')
        car=request.POST.get('carmodel')
        cost=request.POST.get('carprice')
        obj=CarItem(name=brand,model=car,price=cost)
        obj.save()
        result=CarItem.objects.all()[::-1]
        return render(request,'home.html',{'data':result})
    return render(request,'home.html')


def movies(request):
    result=MovItem.objects.all()[::-1]
    if request.method=="POST":
        nm=request.POST.get('mvnm')
        yor=request.POST.get('yor')
        dr=request.POST.get('mvdr')
        obj=MovItem(name=nm,year=yor,dir=dr)
        obj.save()
        result=MovItem.objects.all()[::-1]
        return render(request,'movies.html',{'data':result})
    return render(request,'movies.html')

def single(request,rid):
    if MovItem.objects.filter(id=rid).exists():
        obj=MovItem.objects.get(id=rid)
        d={
            'data':obj
        }
        return render(request,'single.html',d)
    return render(request,'single.html')