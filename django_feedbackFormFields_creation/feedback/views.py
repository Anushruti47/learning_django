from django.shortcuts import render
from .forms import FeedbackForm

def feedback_form_view(request):
    form = FeedbackForm()
    context = {
        'form': form,
        'page_title': 'Provide Feedback'
    }
    return render(request, 'feedback_page.htm', context)

def homepage_view(request):
    return render(request, 'homepage.html')
