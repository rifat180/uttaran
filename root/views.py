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
    name = name[0].name if name else 'Uttaran'
    missions = Mission.objects.all()
    visions = Vision.objects.all()
    goals = Goal.objects.all()
    testimonials = Testimonial.objects.all()
    event_pictures = EventPicture.objects.all()
    context = {
        'title': 'Welcome | ' + name,
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
    name = LibraryName.objects.all()
    name = name[0].name if name else 'Uttaran'
    all_books = Book.objects.all()
    context = {
        'title': 'Books | ' + name,
        'name': name,
        'active_link': 'books',
        'all_books': all_books
    }
    return render(request, template_name, context)

def book_details(request, id):
    template_name = 'root/book_details.html'
    name = LibraryName.objects.all()
    name = name[0].name if name else 'Uttaran'
    context = {
        'title': 'Book Details | ' + name,
        'name': name,
        'active_link': 'books',
        'book': Book.objects.get(pk=id)
    }
    return render(request, template_name, context)

def members(request):
    template_name = 'root/members.html'
    name = LibraryName.objects.all()
    name = name[0].name if name else 'Uttaran'
    all_members = Member.objects.all()
    advisors = [ member for member in all_members if member.designation.lower() == 'advisor' ]
    committee = [member for member in all_members if member.designation.lower() == 'committee member']
    members = [member for member in all_members if member.designation.lower()== 'member']
    context = {
        'title': 'Members | ' + name,
        'name': name,
        'active_link': 'members',
        'advisors': advisors,
        'committee': committee,
        'members': members
    }
    return render(request, template_name, context)

def member_details(request, id):
    template_name = 'root/member_details.html'
    name = LibraryName.objects.all()
    name = name[0].name if name else 'Uttaran'
    context = {
        'title': 'Member Details | ' + name,
        'name': name,
        'active_link': 'members',
        'member': Member.objects.get(pk = id)
    }
    return render(request, template_name, context)

def about(request):
    template_name = 'root/about.html'
    name = LibraryName.objects.all()
    name = name[0].name if name else 'Uttaran'
    paragraph = About.objects.all()
    context = {
        'title': 'About | ' + name,
        'name': name,
        'active_link': 'about',
        'paragraphs': paragraph,
    }
    return render(request, template_name, context)

def contacts(request):
    template_name = 'root/contacts.html'
    name = LibraryName.objects.all()
    name = name[0].name if name else 'Uttaran'
    context = {
        'title': 'Contacts | ' + name,
        'name': name,
        'active_link': 'contacts',
    }
    return render(request, template_name, context)
