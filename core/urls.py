from django.urls import path
from .views import DebugCodeView

urlpatterns = [
    path('debug/', DebugCodeView.as_view(), name='debug-code'),
]