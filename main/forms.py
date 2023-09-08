from django import forms
from .models import Answer

class AnswerForm(forms.ModelForm):
    answer = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Your answer here...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",
    )

    class Meta:
        model = Answer
        exclude = ("question","participant")