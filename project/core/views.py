# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView

from . import models as core_models


class Index(LoginRequiredMixin, ListView):
    model = core_models.Produto
    template_name = 'core/pages/index.html'


class ProductDetail(LoginRequiredMixin, DetailView):
    model = core_models.Produto
    template_name = 'core/pages/detail.html'
