from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RequestForm
from .models import Request, Service

@login_required
def create_request(request):
    if request.method == "POST":
        form = RequestForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("someapp:main")
    else:
        form = RequestForm(user=request.user)
    return render(request, "request_form.html", {"form": form})

def main(request):
    return render(request, "main.html")

@login_required
def my_requests(request):
    requests = Request.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "my_requests.html", {"requests": requests})

def services(request):
    services = Service.objects.all()
    return render(request, "services.html", {"services": services})