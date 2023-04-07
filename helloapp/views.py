from django.shortcuts import render

# Create your views here.

def helloappfunc(request):
    message = {
        "title":"helloapp",
        "text": "hello",
    }
    return render(request,'index.html',message)
