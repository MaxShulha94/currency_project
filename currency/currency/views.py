from django.http.response import HttpResponse

from .models import Rate, ContactUs


def rate_list(request):
    results = []
    rates = Rate.objects.all()

    for rate in rates:
        results.append(
            f'ID: {rate.id}, buy: {rate.buy}, sell: {rate.sell}, type: {rate.type}, '
            f'source: {rate.source}, created: {rate.created} <br>'
        )

    return HttpResponse(str(results))


def contact_list(request):
    results = []
    contacts = ContactUs.objects.all()

    for contact in contacts:
        results.append(
            f'ID: {contact.id}, mail: {contact.email_from}, subject: {contact.subject}, message: {contact.message}<br>'
        )

    return HttpResponse(str(results))
