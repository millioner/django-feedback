from django import forms

from feedback.models import Feedback, AnonymousFeedback

class FeedbackForm(forms.ModelForm):
    next = forms.CharField(required=False, widget=forms.HiddenInput)
    class Meta:
        model = Feedback
        exclude = ('user',)


class AnonymousFeedbackForm(forms.ModelForm):
    next = forms.CharField(required=False, widget=forms.HiddenInput)
    class Meta:
        model = AnonymousFeedback
        exclude = ('user',)

