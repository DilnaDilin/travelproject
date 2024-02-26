from django.http import HttpResponse
from django.shortcuts import render
from .models import Destinations
# Create your views here.
def demo(request):
    obj=Destinations.objects.all()
    return render(request,'index.html', {'results':obj})