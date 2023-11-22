from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Rate, ContactUs


def rate_list(request):
    rates = Rate.objects.all()
    context = {'rates': rates}


    return render(request, 'rate_list.html', context)


def contact_list(request):
    contacts = ContactUs.objects.all()
    context = {'contacts': contacts}


    return render(request, 'contact_list.html', context)



