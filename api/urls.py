from django.urls import path
from .views import ReferenceAPIView

urlpatterns = [
    path('', ReferenceAPIView.as_view()),
]
