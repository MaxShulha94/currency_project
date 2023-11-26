from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Rate, ContactUs, Source
from .forms import RateForm, SourceForm


def rate_list(request):
    rates = Rate.objects.all()
    context = {'rates': rates}

    return render(request, 'rate_list.html', context)


def create_rate(request):
    if request.method == 'POST':
        form = RateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate_list/')
    else:
        form = RateForm
    context = {
        'form': form
    }
    return render(request, 'rate_create.html', context)


def update_rate(request, pk):
    rate = get_object_or_404(Rate, id=pk)
    if request.method == 'POST':
        form = RateForm(data=request.POST, instance=rate)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate_list/')
    elif request.method == 'GET':
        form = RateForm(instance=rate)
    context = {
        'form': form
    }
    return render(request, 'rate_update.html', context)


def delete_rate(request, pk):
    rate = get_object_or_404(Rate, id=pk)
    if request.method == 'GET':
        context = {
            'rate': rate
        }
        return render(request, 'rate_delete.html', context)
    elif request.method == 'POST':
        rate.delete()
    return HttpResponseRedirect('/rate_list/')


def retrieve_rate(request, pk):
    rate = get_object_or_404(Rate, id=pk)
    context = {
        'rate': rate
    }
    return render(request, 'rate_retrieve.html', context)


def contact_list(request):
    contacts = ContactUs.objects.all()
    context = {'contacts': contacts}

    return render(request, 'contact_list.html', context)


def source_list(request):
    sources = Source.objects.all()
    context = {'sources': sources}

    return render(request, 'source_list.html', context)


def create_source(request):
    if request.method == 'POST':
        form = SourceForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source_list/')
    else:
        form = SourceForm
    context = {
        'form': form
    }
    return render(request, 'source_create.html', context)


def update_source(request, pk):
    source = get_object_or_404(Source, id=pk)
    if request.method == 'POST':
        form = SourceForm(data=request.POST, instance=source)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source_list/')
    elif request.method == 'GET':
        form = SourceForm(instance=source)
    context = {
        'form': form
    }
    return render(request, 'source_update.html', context)


def delete_source(request, pk):
    source = get_object_or_404(Source, id=pk)
    if request.method == 'GET':
        context = {
            'source': source
        }
        return render(request, 'source_delete.html', context)
    elif request.method == 'POST':
        source.delete()
    return HttpResponseRedirect('/source_list/')


def retrieve_source(request, pk):
    source = get_object_or_404(Source, id=pk)
    context = {
        'source': source
    }
    return render(request, 'source_retrieve.html', context)
