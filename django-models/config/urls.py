from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("relationship_app.urls")),
    path("", include("relationship_app.urls")),
]
