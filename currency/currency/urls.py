from django.urls import path

from .views import (
    rate_list,
    contact_list,
)

urlpatterns = [
    path('rate_list/', rate_list),
    path('contact_list/', contact_list),
]
