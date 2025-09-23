from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Home")
    return render(request,'index.html',{'title':'Home'})

def about(request):
    # return HttpResponse("about US")
    return render(request,'about.html',{'title':'about'})

def contact(request):
    # return HttpResponse('contact Us')
    return render(request,'contact.html',{'title':'Contact'})

def career(request):
    return render(request,'career.html',{'title':'Career'})