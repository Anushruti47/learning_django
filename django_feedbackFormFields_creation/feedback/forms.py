from django import forms

class FeedbackForm(forms.Form):
    FEEDBACK_CHOICES = [
        ('general', 'General Inquiry'),
        ('bug', 'Bug Report'),
        ('suggestion', 'Suggestion'),
    ]
    name = forms.CharField(label='Your Full Name', max_length=100)
    email = forms.EmailField(label='Your Email Address')
    rating = forms.IntegerField(
        label='Rating (1-5)',
        min_value=1,
        max_value=5,
        required=False
    )
    feedback_type = forms.ChoiceField(
        label='Type of Feedback',
        choices=FEEDBACK_CHOICES,
        initial='general'
    )
    message = forms.CharField(
        label='Your Message',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})
    )
    send_copy = forms.BooleanField(
        label='Send a copy to yourself?',
        required=False
    )
    