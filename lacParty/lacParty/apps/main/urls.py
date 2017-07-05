from django.conf.urls import url
from .views import LoginView, HomeView

urlpatterns = [
    url(r'^$', LoginView.as_view(), name="Login"),
    url(r'^home$', HomeView.as_view(), name="home"),
]
