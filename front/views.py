from django.http import HttpResponse
import os
from django.shortcuts import render

def front(request):
    return render(request,'front/base.html')