from django.contrib import admin

from . import models as core_models

# Register your models here.
admin.site.register(core_models.Produto)
admin.site.register(core_models.Marca)
admin.site.register(core_models.Categoria)
