from django.urls import path

from . import views

urlpatterns = [
    path("",
         views.Index.as_view(),
         name="index"
         ),

    path("produto/<slug:slug>",
         view=views.ProductDetail.as_view(),
         name="produto_detail"
         )
]
