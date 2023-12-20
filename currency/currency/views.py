from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.mail import send_mail
from django.http import HttpResponseForbidden
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


class RateUpdateView(UserPassesTestMixin, UpdateView):
    model = Rate
    form_class = RateForm
    success_url = reverse_lazy('rate-list')
    template_name = 'rate_update.html'

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return HttpResponseForbidden("You have no permission for this operation.")


class RateDeleteView(UserPassesTestMixin, DeleteView):
    model = Rate
    success_url = reverse_lazy('rate-list')
    template_name = 'rate_delete.html'

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return HttpResponseForbidden("You have no permission for this operation.")


class RateDetailsView(UserPassesTestMixin, DetailView):
    model = Rate
    template_name = 'rate_retrieve.html'
    login_url = reverse_lazy('login')

    def test_func(self):
        return self.request.user.is_authenticated


class ContactUsListView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'contact_list.html'


class ContactUsCreateView(CreateView):
    form_class = ContactUsForm
    success_url = reverse_lazy('index')
    template_name = 'contact_create.html'

    def form_valid(self, form):
        recipient = 'settings.EMAIL_HOST_USER'
        subject = 'User contact us'
        body = f'''
        Name: {form.cleaned_data['name']}
        Email: {form.cleaned_data['email_from']}
        Subject: {form.cleaned_data['subject']}
        Message: {form.cleaned_data['message']}
        Body: {form.cleaned_data['body']}
        '''
        send_mail(
            subject,
            body,
            recipient,
            ['recipient'],
            fail_silently=False,
        )
        return super().form_valid(form)


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
