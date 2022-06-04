from socketserver import ForkingMixIn
from django.urls import include
from django.urls import path
from .views import frontpage_view


urlpatterns = [
    path("", frontpage_view, name="frontpage"),
]
