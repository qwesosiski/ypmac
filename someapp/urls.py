from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = "someapp"

urlpatterns = [
    path("", views.main, name="main"),
    path("request/new/", views.create_request, name="create_request"),
    path("accounts/login/",LoginView.as_view(success_url=reverse_lazy("someapp:main")),name="login"),
    path("my-requests/", views.my_requests, name="my_requests"),
    path("logout/", LogoutView.as_view(next_page="someapp:main"), name="logout"),
    path("services/", views.services, name="services"),

]
