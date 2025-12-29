from django import forms

class SongRequestForm(forms.Form):
    name=forms.CharField(label="Your Name",max_length=100)
    song=forms.CharField(label="Your Song Request",max_length=200)
    