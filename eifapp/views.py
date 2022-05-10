from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def devotionals(request):
    return render(request, 'devotionals.html')

def sermons(request):
    return render(request, 'sermons.html')
