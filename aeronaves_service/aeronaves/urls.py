from django.urls import path

from .views import ApiRootView, FiltrosView, MatriculasView

urlpatterns = [
    path('', ApiRootView.as_view(), name='api-root'),
    path('matriculas', MatriculasView.as_view(), name='matriculas'),
    path('filtros', FiltrosView.as_view(), name='filtros'),
]
