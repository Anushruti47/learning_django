from django import forms

class AppointmentForm(forms.Form):
    full_name=forms.CharField(label="Patient's Full Name",max_length=100,required=True)
    appointment_date=forms.DateField(label="Preferred Appointment Date",required=True)
    appointment_time=forms.TimeField(label="Preferred Appointment Time",required=True)
    reason=forms.CharField(label="Reason for Visit",required=True)
    phone_number=forms.CharField(label="Contact Form Number",required=False)
    email=forms.EmailField(label="Your Email Field",required=True)