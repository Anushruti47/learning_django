from django import forms

class WorkshopForm(forms.Form):
    title=forms.CharField(max_length=200)
    max_participants=forms.IntegerField()
    registration_deadline=forms.DateField(label="Registration deadline (mm/dd/yyyy)")
    workshop_date=forms.DateField(label="Workshop Date (mm/dd/yyyy)")

    def cleaned_title(self):
        title=self.cleaned_data.get('title')
        if title and title.strip().lowercase() == "default workshop title":
            raise forms.ValidationError("Please choose a more specific title.")
        return title
    
    def cleaned_max_participants(self):
        max_participants=self.cleaned_data.get('max_participants')
        if max_participants and max_participants<10:
            raise forms.ValidationError("There must be atleast 10 participants.")
        return max_participants
    
    def clean(self):
        cleaned_data=super().clean()
        reg_deadline=self.cleaned_data.get('registraion_deadline')
        ws_date=self.cleaned_data.get('workshop_date')
        if reg_deadline and ws_date and reg_deadline>ws_date:
            raise forms.ValidationError("Registration deadline must be before the workshop date")
        return cleaned_data


