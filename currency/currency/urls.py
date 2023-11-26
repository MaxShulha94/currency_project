from django.urls import path

from .views import (
    rate_list,
    create_rate,
    update_rate,
    delete_rate,
    retrieve_rate,
    contact_list,
    source_list,
    create_source,
    update_source,
    delete_source,
    retrieve_source,
)

urlpatterns = [
    path('rate_list/', rate_list),
    path('rate_create/', create_rate),
    path('rate_update/<int:pk>/', update_rate),
    path('rate_delete/<int:pk>/', delete_rate),
    path('rate_retrieve/<int:pk>/', retrieve_rate),
    path('contact_list/', contact_list),
    path('source_list/', source_list),
    path('source_create/', create_source),
    path('source_update/<int:pk>/', update_source),
    path('source_delete/<int:pk>/', delete_source),
    path('source_retrieve/<int:pk>/', retrieve_source),
]
