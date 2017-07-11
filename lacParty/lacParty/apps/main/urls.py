from django.conf.urls import url
from . import views
from .views import  HomeView

urlpatterns = [
    url(r'^home$', HomeView.as_view(), name="home"),
    url(r'^form$', views.FormView, name="form"),
    url(r'^upload$', views.UploadView, name="upload"),
]
