from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import ProductFeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = ProductFeedbackForm(request.POST)
        if form.is_valid():
            # Normally, save data or take some action here
            return render(request, 'thank_you.html')
    else:
        form = ProductFeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})

def thank_you_view(request):
    return render(request,"thank_you.html")
