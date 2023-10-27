# from django.http import HttpResponse
from django.shortcuts import render

from . import models as core_models


def index(request):
    produtos = core_models.Produto.objects.all()
    return render(
        request,
        'core/pages/index.html',
        {'produtos': produtos}
    )
