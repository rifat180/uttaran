from django.shortcuts import render
from .models import (
    LibraryName,
    Mission,
    Vision,
    Goal,
    Testimonial,
    EventPicture,
    Book,
    Member,
    About
)

# Create your views here.
def home(request):
    template_name = 'root/home.html'
    context = {
        'title': 'Welcome | Uttron',
        'name': LibraryName.objects.all()[-1],
        'active_link': 'home',
        'missions': Mission.objects.all(),
        'visions': Vision.objects.all(),
        'goals': Goal.objects.all(),
        'testi_len': 3,
        'length': 3
    }
    return render(request, template_name, context)

def books(request):
    template_name = 'root/books.html'
    context = {
        'title': 'Books | Uttron',
        'name': LibraryName.objects.all()[-1],
        'active_link': 'books',
        'all_books': Book.objects.all()
    }
    return render(request, template_name, context)

def book_details(request):
    template_name = 'root/book_details.html'
    context = {
        'title': 'Book Details | Uttron',
        'name': LibraryName.objects.all()[0],
        'active_link': 'books',
        'book': Book.objects.get(pk=id)
    }
    return render(request, template_name, context)

def members(request):
    template_name = 'root/members.html'
    all_members = Member.objects.all()
    advisors = [ member for member in all_members if member.designation.lower() == 'advisor' ]
    committee = [member for member in all_members if member.designation.lower() == 'committee member']
    members = [member for member in all_members if member.designation.lower()== 'member']
    context = {
        'title': 'Members | Uttron',
        'name': LibraryName.objects.all()[-1],
        'active_link': 'members',
        'advisors': advisors,
        'committee': committee,
        'members': members
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
