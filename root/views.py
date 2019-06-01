from django.shortcuts import render

# Create your views here.
def home(request):
    template_name = 'root/home.html'
    context = {
        'title': 'Welcome | Uttron',
        'name': 'Uttron'
    }
    return render(request, template_name, context)
    