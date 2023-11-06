from django.urls import path

from . import views as core_views

urlpatterns = [
    path("",
         core_views.Index.as_view(),
         name="index"
         ),

    path("produto/<slug:slug>",
         view=core_views.ProductDetail.as_view(),
         name="produto_detail"
         )
]
