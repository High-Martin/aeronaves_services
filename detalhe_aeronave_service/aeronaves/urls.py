from django.urls import path

from .views import ApiRootView, AeronaveDetailView

urlpatterns = [
    path('', ApiRootView.as_view(), name='api-root'),
    path('aeronaves/<str:matricula>/', AeronaveDetailView.as_view(), name='aeronave-detail'),
]
