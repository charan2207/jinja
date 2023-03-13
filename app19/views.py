from django.shortcuts import render

# Create your views here.
def jinja(request):
    dd={'loc':'bnglor','contact':152526}
    return render(request,'jinja',context=dd)