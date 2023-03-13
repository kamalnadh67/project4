from django.shortcuts import render

# Create your views here.
def virat(request):
    d={'name':'kamal'}
    return render(request,'one.html',context=d)
