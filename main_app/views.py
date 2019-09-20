from django.shortcuts import render
from .models import Widget

# Create your views here.

def home(request): 
    widgets = Widget.objects.all( )

# if request.method == ‘POST’:
#     form = PokemonForm(reques.POST )
#         if form.is_valid( )
#             form.save( )
#             return redirect(‘home’)    

# else:
#     form = PokemonForm( )

#{‘form’: form} ,     
    return render(request, 'home.html', {'widgets': widgets})