from django import forms
from .models import Advising

decisions = (
    (0, 'Approve'),
    (1, 'Deny'),
)


class SubmitAdvisingForm(forms.ModelForm):
    class Meta:
        model = Advising
        fields = (
            'semester',
            'major',
            'QPA',
            'GPA',
            'intended_courses',
            'currently_enrolled',
            'completed_courses',
            'total_credits'
        )

class ApproveDenyForm(forms.Form):
    decision = forms.ChoiceField(choices = decisions)


