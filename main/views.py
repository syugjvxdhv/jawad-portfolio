from django.shortcuts import render
from .models import ContactMessage
from .models import Project


# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def projects(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'projects.html', {'projects': projects})
def contact(request):
    

    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        return render(request,'contact.html',{'success':True})

    return render(request,'contact.html')