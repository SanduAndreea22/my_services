from django.shortcuts import render

def home(request):
    return render(request, 'website/home.html')

def services(request):
    return render(request, 'website/services.html')

def contact(request):
    return render(request, 'website/contact.html')

def projects(request):
    return render(request, 'website/projects.html')

def faq(request):
    return render(request, "website/faq.html")

def reviews(request):
    return render(request, "website/reviews.html")