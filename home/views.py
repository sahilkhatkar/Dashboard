from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):

    # if request=="GET":
    #     return render(request, 'dashboard.html')
    return render(request, 'home.html')

def dashboard(request):
    # return HttpResponse("hello")
    return render(request, 'dashboard.html')