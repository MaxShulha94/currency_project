from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView

from currency.forms import RateForm, ContactUsForm, SourceForm
from currency.models import Rate, ContactUs, Source
from currency.tasks import send_email_in_background


class RateListView(ListView):
    queryset = Rate.objects.all().select_related('source').all()
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


def _send_email(form):
    subject = 'User contact us'
    body = f'''
    Name: {form.cleaned_data['name']}
    Email: {form.cleaned_data['email_from']}
    Subject: {form.cleaned_data['subject']}
    Message: {form.cleaned_data['message']}
    Body: {form.cleaned_data['body']}
    '''
    send_email_in_background.apply_async(
            kwargs={
                'subject': subject,
                'body': body
            }
        )


class ContactUsCreateView(CreateView):
    form_class = ContactUsForm
    success_url = reverse_lazy('index')
    template_name = 'contact_create.html'

    def form_valid(self, form):
        redirect = super().form_valid(form)

        _send_email(form)

        return redirect


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
