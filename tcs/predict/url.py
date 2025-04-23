from django.contrib import admin
from django.urls import path
from .views import *
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",TemplateView.as_view(template_name='index.html')),
    path(r"predict/",predict.as_view())
] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

