from django.shortcuts import render, get_object_or_404

# Create your views here.
def Home(request):
    template = 'index.html'
    return render( request, template)
