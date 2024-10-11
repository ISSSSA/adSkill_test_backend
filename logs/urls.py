from django.urls import path

from .views import get_logs, get_log_detail, create_log

urlpatterns = [
    path('', get_logs, name='get_logs'),
    path('<str:log_id>/', get_log_detail, name='get_log_detail'),
    path('content/create/', create_log, name='create_log'),
]
