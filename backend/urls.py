from django.contrib import admin
from django.urls import include, path

from .api import api

urlpatterns = [
    path('', include('backend.core.urls', namespace='core')),
    path('expense/', include('backend.expense.urls', namespace='expense')),
    path('api/v1/', api.urls),
    path('admin/', admin.site.urls),
]
