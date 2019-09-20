from django.shortcuts import render, redirect
from .forms import WidgetForm
from .models import Widget

# Create your views here.

def home(request): 
    widgets = Widget.objects.all( )

    if request.method == 'POST':
        form = WidgetForm(reques.POST)
        if form.is_valid( ):
            form.save( )
        return redirect('home')    

    else:
        form = WidgetForm( )

    return render(request, 'home.html', {'form': form, 'widgets': widgets})