from django.shortcuts import render
from .forms import FeedbackForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def submit_feedback_form(request):
    if request.method == 'POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get('name','Anonymous')
            message=form.cleaned_data.get('message','No message provided')
        context={
            'name':name,
            'message':message
        }
        return render(request,"feedback_confirmation_form.html",context)
    else:
        form=FeedbackForm()
    return render(request,"submit_feedback_form.html",{'form':form})



