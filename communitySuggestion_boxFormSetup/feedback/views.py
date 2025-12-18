from django.shortcuts import render
from .forms import SuggestionForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def suggestion_form_view(request):
    form=SuggestionForm()
    context={
        'form_title':'Community Suggestion Box',
        'form':form
    }
    return render(request,"suggestion_page.html",context)

def homepage(request):
    return render(request,"homepage.html")