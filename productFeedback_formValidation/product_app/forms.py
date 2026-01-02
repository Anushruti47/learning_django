from django import forms

class ProductFeedbackForm(forms.Form):
    product_name = forms.CharField(max_length=100)
    rating = forms.ChoiceField(choices=[(str(i), str(i)) for i in range(1, 6)])
    feedback_text = forms.CharField()
    reason_for_low_rating = forms.CharField(required=False)

    def clean_product_name(self):
        name = self.cleaned_data.get('product_name')
        if name and name.strip().lower() == 'test product':
            raise forms.ValidationError("Product name cannot be 'Test Product'.")
        return name

    def clean_feedback_text(self):
        feedback = self.cleaned_data.get('feedback_text')
        if feedback and len(feedback.strip()) < 10:
            raise forms.ValidationError("Feedback must be at least 10 characters long.")
        return feedback

    def clean(self):
        cleaned_data = super().clean()
        rating = cleaned_data.get('rating')
        reason = cleaned_data.get('reason_for_low_rating')

        if rating in ['1', '2'] and not reason:
            self.add_error('reason_for_low_rating', "Please provide a reason for your low rating.")
        return cleaned_data
