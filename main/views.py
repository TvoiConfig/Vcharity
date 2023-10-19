from django.shortcuts import render
from .models import *
from .forms import RecordForm

def index(request):
    return render(request, 'main/index.html')

def contact(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RecordForm()
        
    return render(request, 'main/contact.html', {'form': form})