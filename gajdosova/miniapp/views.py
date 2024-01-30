import random

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def models_list(reguest):
    random_number = random.randint(1, 100)
    return HttpResponse(f"random number {random_number}")