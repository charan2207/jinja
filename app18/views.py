from django.shortcuts import render

# Create your views here.
def jinja(request):

    d={'name':'charan', 'age':54}
    return render (request,'jinja.html',context=d)
