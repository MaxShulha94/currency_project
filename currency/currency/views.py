from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView

from .forms import RateForm, ContactUsForm, SourceForm
from .models import Rate, ContactUs, Source


class RateListView(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'


class RateCreateView(CreateView):
    form_class = RateForm
    success_url = reverse_lazy('rate-list')
    template_name = 'rate_create.html'


class RateUpdateView(UpdateView):
    model = Rate
    form_class = RateForm
    success_url = reverse_lazy('rate-list')
    template_name = 'rate_update.html'


class RateDeleteView(DeleteView):
    model = Rate
    success_url = reverse_lazy('rate-list')
    template_name = 'rate_delete.html'


class RateDetailsView(DetailView):
    model = Rate
    template_name = 'rate_retrieve.html'


class ContactUsListView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'contact_list.html'


class ContactUsCreateView(CreateView):
    form_class = ContactUsForm
    success_url = reverse_lazy('contact-list')
    template_name = 'contact_create.html'


class ContactUsUpdateView(UpdateView):
    model = ContactUs
    form_class = ContactUsForm
    success_url = reverse_lazy('contact-list')
    template_name = 'contact_update.html'


class ContactUsDeleteView(DeleteView):
    model = ContactUs
    success_url = reverse_lazy('contact-list')
    template_name = 'contact_delete.html'


class ContactUsDetailsView(DetailView):
    model = ContactUs
    template_name = 'contact_retrieve.html'


class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class SourceCreateView(CreateView):
    form_class = SourceForm
    success_url = reverse_lazy('source-list')
    template_name = 'source_create.html'


class SourceUpdateView(UpdateView):
    model = Source
    form_class = SourceForm
    success_url = reverse_lazy('source-list')
    template_name = 'source_update.html'


class SourceDeleteView(DeleteView):
    model = Source
    success_url = reverse_lazy('source-list')
    template_name = 'source_delete.html'


class SourceDetailsView(DetailView):
    model = Source
    template_name = 'source_retrieve.html'


class IndexView(TemplateView):
    template_name = 'index.html'
