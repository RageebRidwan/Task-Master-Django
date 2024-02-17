from django import forms
from .models import Task


class taskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "due_date": forms.DateInput(format="%d/%m/%Y", attrs={"type": "date"}),
        }
