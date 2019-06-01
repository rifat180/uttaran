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
    name = LibraryName.objects.all()
    name = name[0].name if name else 'Uttron'
    missions = Mission.objects.all()
    visions = Vision.objects.all()
    goals = Goal.objects.all()
    testimonials = Testimonial.objects.all()
    event_pictures = EventPicture.objects.all()
    context = {
        'title': 'Welcome | Uttron',
        'name': name,
        'active_link': 'home',
        'missions': missions,
        'visions': visions,
        'goals': goals,
        'testimonials': testimonials,
        'testi_len': len(testimonials),
        'event_pictures': event_pictures,
        'length': len(event_pictures)
    }
    return render(request, template_name, context)

def books(request):
    template_name = 'root/books.html'
    all_books = Book.objects.all()
    context = {
        'title': 'Books | Uttron',
        'name': 'Uttron',
        'active_link': 'books',
        'all_books': all_books
    }
    return render(request, template_name, context)

def book_details(request):
    template_name = 'root/book_details.html'
    context = {
        'title': 'Book Details | Uttron',
        'name': 'Uttron',
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
        'name': 'Uttron',
        'active_link': 'members',
        'advisors': advisors,
        'committee': committee,
        'members': members
    }
    return render(request, template_name, context)

def member_details(request):
    template_name = 'root/member_details.html'
    context = {
        'title': 'Member Details | Uttron',
        'name': 'Uttron',
        'active_link': 'members',
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'root/about.html'
    context = {
        'title': 'About | Uttron',
        'name': 'Uttron',
        'active_link': 'about',
    }
    return render(request, template_name, context)

def contacts(request):
    template_name = 'root/contacts.html'
    context = {
        'title': 'Contacts | Uttron',
        'name': 'Uttron',
        'active_link': 'contacts',
    }
    return render(request, template_name, context)
