from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.utils.text import slugify
# Create your models here.


class Incubatee(AbstractUser):
    STARTUP_SECTOR_CHOICES = [
        ('Edutech', 'EduTech'),
        ('FinTech', 'FinTech'),
        ('AI-ML', 'AI-ML'),
        ('Healthcare', 'Healthcare'),
        ('E-Commerce', 'E-Commerce'),
        ('AR-VR', 'AR-VR'),
        ('Finserv', 'Finserv'),
        ('Gaming', 'Gaming'),
        ('Robotics', 'Robotics'),
        ('Electric Vehicles', 'Electric Vehicles'),
        ('Renewable Energy', 'Renewable Energy'),
        ('SaaS', 'SaaS'),
        ('Hardware', 'Hardware'),
        ('Others', 'Others'),
        # Add more choices as needed
    ]
    CURRENT_STATUS_CHOICES = [
        ('Current', 'Current'),
        ('Graduated', 'Graduated'),
        # Add more choices as needed
    ]
    username = None
    founder_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, unique=True)
    company_website = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='static/assets/incubatee/logo')
    company_description = models.TextField()
    startup_sector = models.CharField(
        max_length=100, choices=STARTUP_SECTOR_CHOICES)
    startup_scheme = models.CharField(max_length=100)
    current_status = models.CharField(max_length=100, choices=CURRENT_STATUS_CHOICES)
    founder_image = models.ImageField(upload_to='static/assets/incubatee/founder_image')
    free_slots = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    charges = models.FloatField(null=True, blank=True)
    lock = models.IntegerField(default=0, null=True, blank=True)
    USERNAME_FIELD = 'company_name'
    objects = UserManager()
    # REQUIRED_FIELDS = ['founder_name','company_name','company_website','logo','company_description','startup_sector','startup_scheme','current_status','founder_image']


class Features(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='static/assets/cards')
    bullets = models.TextField(blank=True, null=True)

    def bullets_list(self):
        if self.bullets:
            return self.bullets.split('\n')
        return []

    def __str__(self):
        return self.title
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/assets/team')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class VisionMission(models.Model):
    vision = models.TextField()
    mission = models.TextField()

    def __str__(self):
        return self.vision
    
    
class Stat(models.Model):
    startups = models.IntegerField()
    current = models.IntegerField()
    graduated = models.IntegerField()
    image = models.ImageField(upload_to='static/assets/stats', null=True, blank=True)

    def __str__(self):
        return str(self.startups) + " Startups, " + str(self.current) + " Current, " + str(self.graduated) + " Graduated"
    
class News(models.Model):
    image = models.ImageField(upload_to='static/assets/news')
    title = models.CharField(max_length=1000)
    day = models.IntegerField()
    month = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='static/assets/testimonial')
    description = models.TextField()

    def __str__(self):
        return self.name    
   
class Facility(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/assets/facility')
    def __str__(self):
        return self.name
    
class Project(models.Model):
    projectName = models.CharField(max_length=200)
    projectDescription = models.TextField(blank=True, null=True)
    projectLink = models.CharField(max_length=200, blank=True, null=True)
    people = models.TextField()
    image = models.ImageField(upload_to='static/assets/project')
    def __str__(self):
        return self.name
    
class ProgrammeYear(models.Model):
    yearNo = models.IntegerField()
    programme = models.ForeignKey('Programme', on_delete=models.CASCADE)
    incubatees = models.ManyToManyField(Incubatee, blank=True)
    projects = models.ManyToManyField(Project, blank=True)
    def __str__(self):
        return str(self.programme) + '-' + str(self.yearNo)
    
class Programme(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    about = models.TextField(null=True, blank=True)
    banner = models.ImageField(upload_to='static/assets/banner')
    objectives = models.TextField(null=True, blank=True)
    broadcovered = models.TextField(null=True, blank=True)
    broadnotcovered = models.TextField(null=True, blank=True)
    eligible = models.TextField(null=True, blank=True)
    noteligible = models.TextField(null=True, blank=True)
    guidelines = models.TextField(null=True, blank=True)
    facilities = models.ManyToManyField(Facility)
    benefits = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=1000, null=True, blank=True)

    def get_slug(self):
        return slugify(self.title)
    
    def __str__(self):
        return self.title
    
class Banner(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/assets/banner')
    def __str__(self):
        return self.title
    
class Partner(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/assets/partners')
    website = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Partner_type(models.Model):
    name = models.CharField(max_length=200)
    partners = models.ManyToManyField(Partner)
    def __str__(self):
        return self.name
    
class Count(models.Model):
    name = models.CharField(max_length=200)
    count = models.IntegerField()
    def __str__(self):
        return self.name + ' ' + str(self.count)
    
class Image(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/assets/images')
    def __str__(self):
        return self.name
    
class InfraFacility(models.Model):
    name = models.CharField(max_length=200)
    imgs = models.ManyToManyField(Image)
    def __str__(self):
        return self.name
    
class IotDevice(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/assets/iot')
    desc = models.TextField()
    def __str__(self):
        return self.name
    
class Mentor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to='static/assets/mentors')
    linkedin = models.CharField(max_length=100, null=True, default='#')
    def __str__(self):
        return self.name
    
class Mentor_type(models.Model):
    name = models.CharField(max_length=200)
    mentors = models.ManyToManyField(Mentor)
    def __str__(self):
        return self.name
    
class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/assets/sponsors')
    website = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True, blank=True)
    about = models.TextField()
    banner = models.ImageField(upload_to='static/assets/banner')
    timeline = models.TextField(null=True, blank=True)
    link = models.CharField(max_length=1000, null=True, blank=True)
    sponsors = models.ManyToManyField(Sponsor, blank=True)
    partners = models.ManyToManyField(Partner, blank=True)
    prize1st = models.TextField(null=True, blank=True)
    prize2nd = models.TextField(null=True, blank=True)
    prize3rd = models.TextField(null=True, blank=True)
    prizeother = models.TextField(null=True, blank=True)
    targetgrp = models.TextField(null=True, blank=True)
    takeaways = models.TextField(null=True, blank=True)

    def get_slug(self):
        return slugify(self.title)
    
    def __str__(self):
        return self.title

