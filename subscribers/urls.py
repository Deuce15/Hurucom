from django.urls import path
from .views import subscribe, send_test_email

urlpatterns = [
    path('subscribe/', subscribe, name='subscribe'),
    path('send-test-email/', send_test_email, name='send_test_email'),
]

