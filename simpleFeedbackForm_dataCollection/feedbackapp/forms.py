from django import forms

class FeedbackForm(forms.Form):
    name=forms.CharField(label="Your Name",max_length=100)
    message=forms.CharField(label="Your Message",max_length=500)