from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from auth_api.views import RegisterView, LoginView

urlpatterns = [
    path('api/v1/login/', LoginView.as_view(), name='token_obtain_pair'),
    path('api/v1/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/register/', RegisterView.as_view(), name='auth_register'),
]