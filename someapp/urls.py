from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView
from . import views

app_name = "someapp"

urlpatterns = [
    path("", views.main, name="base"),
    path("request/new/", views.create_request, name="create_request"),
    path(
        "accounts/login/",
        LoginView.as_view(success_url=reverse_lazy("someapp:base")),
        name="login",
    ),
]
