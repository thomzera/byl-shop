# from django.shortcuts import render
from django.views.generic import DetailView, ListView

from . import models as core_models


class Index(ListView):
    model = core_models.Produto
    template_name = 'core/pages/index.html'


class ProductDetail(DetailView):
    model = core_models.Produto
    template_name = 'core/pages/detail.html'
