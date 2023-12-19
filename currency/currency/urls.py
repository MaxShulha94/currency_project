from django.urls import path


from .views import (
    RateListView,
    RateCreateView,
    RateUpdateView,
    RateDeleteView,
    RateDetailsView,
    ContactUsListView,
    ContactUsCreateView,
    ContactUsUpdateView,
    ContactUsDeleteView,
    ContactUsDetailsView,
    SourceListView,
    SourceCreateView,
    SourceUpdateView,
    SourceDeleteView,
    SourceDetailsView,
)

urlpatterns = [
    path('rate_list/', RateListView.as_view(), name='rate-list'),
    path('rate_create/', RateCreateView.as_view(), name='rate-create'),
    path('rate_update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate_delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),
    path('rate_retrieve/<int:pk>/', RateDetailsView.as_view(), name='rate-retrieve'),
    path('contact_list/', ContactUsListView.as_view(), name='contact-list'),
    path('contact_create/', ContactUsCreateView.as_view(), name='contact-create'),
    path('contact_update/<int:pk>/', ContactUsUpdateView.as_view(), name='contact-update'),
    path('contact_delete/<int:pk>/', ContactUsDeleteView.as_view(), name='contact-delete'),
    path('contact_retrieve/<int:pk>/', ContactUsDetailsView.as_view(), name='contact-retrieve'),
    path('source_list/', SourceListView.as_view(), name='source-list'),
    path('source_create/', SourceCreateView.as_view(), name='source-create'),
    path('source_update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source_delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),
    path('source_retrieve/<int:pk>/', SourceDetailsView.as_view(), name='source-retrieve'),
]
