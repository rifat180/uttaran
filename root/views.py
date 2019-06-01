from django.shortcuts import render

# Create your views here.
def home(request):
    template_name = 'root/home.html'
    context = {
        'title': 'Welcome | Uttron',
        'name': 'Uttron',
        'active_link': 'home',
        'testi_len': 3,
        'length': 3,
    }
    return render(request, template_name, context)

def books(request):
    template_name = 'root/books.html'
    context = {
        'title': 'Welcome | Uttron',
        'name': 'Uttron',
        'active_link': 'books',
    }
    return render(request, template_name, context)

def book_details(request):
    template_name = 'root/book_details.html'
    context = {
        'title': 'Welcome | Uttron',
        'name': 'Uttron',
        'active_link': 'books',
    }
    return render(request, template_name, context)

def members(request):
    template_name = 'root/members.html'
    context = {
        'title': 'Welcome | Uttron',
        'name': 'Uttron',
        'active_link': 'members',
    }
    return render(request, template_name, context)

def member_details(request):
    template_name = 'root/member_details.html'
    context = {
        'title': 'Welcome | Uttron',
        'name': 'Uttron',
        'active_link': 'members',
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'root/about.html'
    context = {
        'title': 'Welcome | Uttron',
        'name': 'Uttron',
        'active_link': 'about',
    }
    return render(request, template_name, context)

def contacts(request):
    template_name = 'root/contacts.html'
    context = {
        'title': 'Welcome | Uttron',
        'name': 'Uttron',
        'active_link': 'contacts',
    }
    return render(request, template_name, context)
