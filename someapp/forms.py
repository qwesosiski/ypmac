from django import forms
from .models import Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ["service", "comment"]
        widgets = {
            "comment": forms.Textarea(attrs={"rows": 3}),
        }

    def __init__(self, data=None, user=None):
        super().__init__(data=data)
        self._user = user

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self._user
        instance.status = 0
        if commit:
            instance.save()
        return instance

