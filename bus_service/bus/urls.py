from django.urls import path

from .views import ApiRootView, DetalheAeronaveView, FiltrosView, MatriculasView

urlpatterns = [
    path('', ApiRootView.as_view(), name='api-root'),
    path('aeronaves/', MatriculasView.as_view(), name='aeronaves'),
    path('aeronaves/filtros/', FiltrosView.as_view(), name='filtros'),
    path('aeronaves/<matricula>/', DetalheAeronaveView.as_view(), name='detalhe'),
]
