from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RequestForm


@login_required
def create_request(request):
    if request.method == "POST":
        form = RequestForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect("someapp:base")
    else:
        form = RequestForm(user=request.user)
    return render(request, "request_form.html", {"form": form})

def main(request):
    return render(request, "base.html")