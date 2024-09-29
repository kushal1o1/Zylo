from django.shortcuts import render

from django.views import View
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'portfolio/index.html')

