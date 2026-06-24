from django.urls import path

from .views import MatriculasView

urlpatterns = [
    path('matriculas', MatriculasView.as_view(), name='matriculas'),
]
