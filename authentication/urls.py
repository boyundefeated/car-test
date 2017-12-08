from django.conf.urls import url

from .views import RegistrationAPIView, LoginAPIView

urlpatterns = [
    # url(r'^user/?$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^user?$', RegistrationAPIView.as_view()),
    url(r'^authentication/login?$', LoginAPIView.as_view()),
]
