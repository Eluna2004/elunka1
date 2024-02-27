import random
from django.http import HttpResponse
from django.shortcuts import render

def models_list(reguest):
    random_number = random.randint(1,   100)
    return HttpResponse(f"random number {random_number}")

def post_list(request):
    random_number = random.randint(1, 100)
    return render(request, 'miniapp1/post_list.html', {'VAR': random_number})
