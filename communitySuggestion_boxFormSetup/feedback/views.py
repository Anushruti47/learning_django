from django.shortcuts import render
from .forms import SuggestionForm
from django.views import csrf_exempt

# Create your views here.
@csrf_exempt
def suggestion_form_view(request):
    form=SuggestionForm()
    context={
        'form_title':'Community Suggestion Box',
        'form':form
    }
