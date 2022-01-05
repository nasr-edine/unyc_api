from django.urls import path
from .views import ReferenceListView
from .views import ListReference
from .views import DetailReference

urlpatterns = [
    # template (html)
    path('template/', ReferenceListView.as_view(), name='references'),

    # API endpoints (json)
    path('', ListReference.as_view()),
    path('<int:pk>/', DetailReference.as_view()),

]
