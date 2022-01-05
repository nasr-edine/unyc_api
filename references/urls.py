from django.urls import path
from .views import ReferenceListView

urlpatterns = [
    path('', ReferenceListView.as_view(), name='references'),
]
