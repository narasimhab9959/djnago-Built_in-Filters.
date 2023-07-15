from django.shortcuts import render

# Create your views here.
import datetime
def filters(request):
    dt=datetime.datetime.now()
    d={'FO':'narasimha is full stack developers', 'c':1,'dt':dt}
    
    return render(request,'filter.html',d)