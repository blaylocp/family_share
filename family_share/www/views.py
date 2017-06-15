from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegistrationForm 

# Create your views here.
def index(request):
    return HttpResponse("HELLO, WORLD. We are up and running <a href='register'>register</a>")

def register(request):
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

    else: 
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})
