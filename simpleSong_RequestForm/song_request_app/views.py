from django.shortcuts import render
from .forms import SongRequestForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def song_request_form_view(request):
    if request.method == "POST":
        form=SongRequestForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get('name','Anonymous')
            song=form.cleaned_data.get('song','No song provided')
        context={
            'name':name,
            'song':song
        }
        return render(request,"confirmation.html",context)
    else:
        form=SongRequestForm()
    return render(request,"song_request.html",{'form':form})
        

