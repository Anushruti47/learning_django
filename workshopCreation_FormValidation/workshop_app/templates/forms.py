from django import forms

class WorkshpForm(forms.Form):
    title=forms.CharField(max_length=200)
    max_participants=forms.IntegerField()
    registration_deadline=forms.DateField()
    workshop_date=forms.DateField()