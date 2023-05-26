import random

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'generator/externally.html')

def description(request):
    return render(request, 'generator/description.html')

def password(request):
    character = list('qwertyuiopasdfghjklzxcvbnm')

    if request.GET.get('uppercase'):
        character.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

    if request.GET.get('number'):
        character.extend(list('1234567890'))

    if request.GET.get('special'):
        character.extend(list('@#$%^&*()'))

    length = int(request.GET.get('length'))
    thepassword = ''
    for i in range(length):
        thepassword += random.choice(character)
    return  render(request, 'generator/password.html', {'password':thepassword})
