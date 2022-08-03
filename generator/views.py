from django.http import HttpResponse
from django.shortcuts import render
import string
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def info(request):
    return render(request, 'generator/info.html')

def password(request):
    chars_lower = list(string.ascii_lowercase)
    chars_upper = list(string.ascii_uppercase)
    chars_special = list(string.punctuation)
    chars_numbers = list('0123456789')
    length = int(request.GET.get('length', 7))
    if request.GET.get('upper', False):
        chars_lower.extend(chars_upper)
    if request.GET.get('special', False):
        chars_lower.extend(chars_special)
    if request.GET.get('number', False):
        chars_lower.extend(chars_numbers)
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(chars_lower)
    return render(request, 'generator/password.html', {'password': thepassword})
