from django import forms

class FeedbackForm(forms.Form):
    name=forms.CharField(max_length=100)
    