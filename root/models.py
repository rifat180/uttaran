from django.db import models
from django.utils import timezone

# Create your models here.

# TODO: Library Name
class LibraryName(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

# TODO: Mission model
class Mission(models.Model):
    mission = models.CharField(max_length = 100)
    def __str__(self):
        return self.mission

# TODO: Vission model
class Vision(models.Model):
    vision = models.CharField(max_length = 100)
    def __str__(self):
        return self.vision

# TODO: Goal Model
class Goal(models.Model):
    goal = models.CharField(max_length = 100)
    def __str__(self):
        return self.goal

# TODO: Testimonial model
class Testimonial(models.Model):
    testimonial = models.TextField(max_length=400, blank=False, null=False)
    writer = models.CharField(max_length = 150)
    picture = models.ImageField()
    def __str__(self):
        return self.writer

# TODO: Event Pictures
class EventPicture(models.Model):
    title = models.CharField(max_length = 200)
    picture = models.ImageField()

    def __str__(self):
        return self.title

# TODO: Define Book model
class Book(models.Model):
    name = models.CharField(max_length = 150, null = False)
    authorName = models.CharField(max_length = 150, default = '', null = False, blank = False)
    photo = models.ImageField(upload_to = 'Book Pictures')
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name

# TODO: Member model
class Member(models.Model):
    options = (
        ('Advisor', 'Advisor'),
        ('Committee Member', 'Committee Member'),
        ('Member', 'Member')
    )
    name = models.CharField(max_length = 100)
    designation = models.CharField(max_length = 50, choices=options)
    photo = models.ImageField(null = False)
    details = models.TextField(null=False, blank=False, default = '')

    def __str__(self):
        return self.name

# TODO: Define Post model
class About(models.Model):
    title = models.CharField(max_length = 200)
    paragraph = models.TextField(null = False, blank = False, default='')

    def __str__(self):
        return self.title
