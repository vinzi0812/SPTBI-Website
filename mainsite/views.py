from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import *
from django.contrib.auth import login, logout, get_user_model
from django.http import JsonResponse

User = get_user_model()

# Create your views here.
def index(request):
    visit_counter = Count.objects.get(name = "Actual")
    visit_add = Count.objects.get(name = "Extra")
    visit_counter.count += 1
    visit_counter.save()
    count_list = str(visit_counter.count + visit_add.count)
    count = list(count_list)
    pg = Programme.objects.all()
    events = Event.objects.all()
    banners = Banner.objects.all()
    objs = Features.objects.all()
    vm = VisionMission.objects.all()
    Partner_types = Partner_type.objects.all()
    stats = Stat.objects.all()
    news = News.objects.all()
    testimonial = Testimonial.objects.all()
    if request.method == 'POST':
        segment_index = request.POST.get('segmentIndex')
        # Implement your logic to decide the URL to redirect to based on segment_index
        # For example, you can use a dictionary or a list to map segment_index to URLs.

        # Redirect to the desired URL
        # Replace 'desired_url' with the URL you want to redirect to
        # return JsonResponse({'redirect_url': 'desired_url'})
    return render(request,'index.html', {'objs': objs, 'vm': vm, 'Partner_types': Partner_types, 'stats': stats, 'news': news, 'testimonial': testimonial, 'pg': pg, 'banners': banners, 'count': count, 'events' : events})

def incubation(request):
    events = Event.objects.all()
    visit_counter = Count.objects.get(name="Actual")
    visit_add = Count.objects.get(name="Extra")
    count_list = str(visit_counter.count + visit_add.count)
    count = list(count_list)
    pg = Programme.objects.all()
    return render(request,'incubation.html', {'pg': pg, 'count': count, 'events' : events})

def currentincubatee(request):
    events = Event.objects.all()
    visit_counter = Count.objects.get(name="Actual")
    visit_add = Count.objects.get(name="Extra")
    count_list = str(visit_counter.count + visit_add.count)
    count = list(count_list)
    choices = [
        'Edutech', 
        'FinTech',
        'AI-ML',
        'Healthcare',
        'E-Commerce',
        'AR-VR',
        'Finserv',
        'Gaming',
        'Robotics',
        'Electric Vehicles',
        'Renewable Energy',
        'SaaS',
        'Hardware',
        'Others',
    ]
    pg = Programme.objects.all()
    if request.method=='POST':
        option = request.POST.get('selected')
        print(option)
        if option == 'all':
            objects_list = User.objects.filter(
                is_superuser=False, current_status='Current')
        else:
            objects_list = User.objects.filter(
                is_superuser=False, current_status='Current', startup_sector=option)
    # Number of objects to show per page
        per_page = 10

        paginator = Paginator(objects_list, per_page)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        objs = page_obj.object_list
        return render(request, 'currentincubatee.html', {'page_obj': page_obj, 'paginator': paginator, 'objs': objs, 'pg': pg, 'count': count, 'choices': choices, 'events' : events})

    objects_list = User.objects.filter(is_superuser=False, current_status='Current')
    # Number of objects to show per page
    per_page = 10

    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    objs = page_obj.object_list
    return render(request,'currentincubatee.html', {'page_obj': page_obj, 'paginator': paginator, 'objs': objs, 'pg': pg, 'count': count, 'choices': choices, 'events' : events})


def graduatedincubatee(request):
    events = Event.objects.all()
    visit_counter = Count.objects.get(name="Actual")
    visit_add = Count.objects.get(name="Extra")
    count_list = str(visit_counter.count + visit_add.count)
    count = list(count_list)
    choices = [
        'Edutech',
        'FinTech',
        'AI-ML',
        'Healthcare',
        'E-Commerce',
        'AR-VR',
        'Finserv',
        'Gaming',
        'Robotics',
        'Electric Vehicles',
        'Renewable Energy',
        'SaaS',
        'Hardware',
        'Others',
    ]
    pg = Programme.objects.all()
    if request.method == 'POST':
        option = request.POST.get('selected')
        print(option)
        if option == 'all':
            objects_list = User.objects.filter(
                is_superuser=False, current_status='Current')
        else:
            objects_list = User.objects.filter(
                is_superuser=False, current_status='Current', startup_sector=option)
    # Number of objects to show per page
        per_page = 10

        paginator = Paginator(objects_list, per_page)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        objs = page_obj.object_list
        return render(request, 'currentincubatee.html', {'page_obj': page_obj, 'paginator': paginator, 'objs': objs, 'pg': pg, 'count': count, 'choices': choices, 'events' : events})
    objects_list = User.objects.filter(
        is_superuser=False, current_status='Graduated')
    # Number of objects to show per page
    per_page = 10

    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    objs = page_obj.object_list
    return render(request, 'graduatedincubatee.html', {'page_obj': page_obj, 'paginator': paginator, 'objs': objs, 'pg': pg, 'count': count, 'choices': choices, 'events' : events})

def pgtemplate(request, page_slug):
    events = Event.objects.all()
    visit_counter = Count.objects.get(name="Actual")
    visit_add = Count.objects.get(name="Extra")
    count_list = str(visit_counter.count + visit_add.count)
    count = list(count_list)
    pg = Programme.objects.all()
    try:
        page_template = Programme.objects.get(slug=page_slug)
        objectives_list = page_template.objectives.split('\n') if page_template.objectives else []
        eligibility_list = page_template.eligible.split('\n') if page_template.eligible else []
        noteligible_list = page_template.noteligible.split('\n') if page_template.noteligible else []
        broadcovered_list = page_template.broadcovered.split('\n') if page_template.broadcovered else []
        broadnotcovered_list = page_template.broadnotcovered.split('\n') if page_template.broadnotcovered else []
        guidelines = page_template.guidelines.split('\n') if page_template.guidelines else []
        benefits = page_template.benefits.split('\n') if page_template.benefits else []
        years = ProgrammeYear.objects.filter(programme=page_template)
        #sort the years
        years = sorted(years, key=lambda x: x.yearNo)
        print(years)
    except Programme.DoesNotExist:
        # Handle the case when the requested page doesn't exist
        page_template = None
        objectives_list = []
        eligibility_list = []
        noteligible_list = []
        broadcovered_list = []
        broadnotcovered_list = []
        guidelines = []
        benefits = []
        years = []
    return render(request, 'pgtemp.html', {'page_template': page_template, 'pg': pg, 'objectives_list': objectives_list, 'eligibility_list': eligibility_list, 'noteligible_list': noteligible_list, 'broadcovered_list': broadcovered_list, 'broadnotcovered_list': broadnotcovered_list, 'guidelines': guidelines, 'benefits': benefits, 'count': count, 'years': years, 'events' : events})

def events(request, page_slug):
    events = Event.objects.all()
    visit_counter = Count.objects.get(name="Actual")
    visit_add = Count.objects.get(name="Extra")
    count_list = str(visit_counter.count + visit_add.count)
    count = list(count_list)
    pg = Programme.objects.all()
    try:
        page_template = Event.objects.get(slug=page_slug)
        if page_template.timeline:
            timeline_list = page_template.timeline.split(
                '\n') if page_template.timeline else []
            timeline =[i.split(":") for i in timeline_list]
        else:
            timeline = [] 
        takeaways = page_template.takeaways.split(
            '\n') if page_template.takeaways else []
        targetgrp = page_template.targetgrp.split(
            '\n') if page_template.targetgrp else []
        conditions = page_template.sponsors.exists()
        print(page_template.prizeother)
        if page_template.prizeother:
            other_list = page_template.prizeother.split(
                '\n') if page_template.timeline else []
            others = [i.split(":") for i in other_list]
        else:
            others = []
    except Programme.DoesNotExist:
        # Handle the case when the requested page doesn't exist
        page_template = None
        timeline = []
        takeaways = []
        targetgrp = []
        others = []
        conditions = False
    return render(request, 'events.html', {'page_template': page_template, 'pg': pg, 'timeline': timeline, 'takeaways': takeaways, 'targetgrp': targetgrp, 'count': count, 'events' : events, 'conditions': conditions, 'others': others})

def virtualincubation(request):
    events = Event.objects.all()
    visit_counter = Count.objects.get(name="Actual")
    visit_add = Count.objects.get(name="Extra")
    count_list = str(visit_counter.count + visit_add.count)
    count = list(count_list)
    pg = Programme.objects.all()
    return render(request,'virtualincubation.html', {'pg': pg, 'count': count, 'events' : events})

def team(request):
    events = Event.objects.all()
    visit_counter = Count.objects.get(name="Actual")
    visit_add = Count.objects.get(name="Extra")
    count_list = str(visit_counter.count + visit_add.count)
    count = list(count_list)
    pg = Programme.objects.all()
    team = Team.objects.all()
    return render(request,'team.html',{'team':team, 'pg': pg, 'count': count, 'events' : events})

def meetingroom(request):
    events = Event.objects.all()
    visit_counter = Count.objects.get(name="Actual")
    visit_add = Count.objects.get(name="Extra")
    count_list = str(visit_counter.count + visit_add.count)
    count = list(count_list)
    pg = Programme.objects.all()
    infraFacility = InfraFacility.objects.all()
    return render(request,'meetingroom.html', {'pg': pg, 'count': count, 'infraFacility': infraFacility, 'events' : events})

def my_custom_error_view(request, exception=None):
    events = Event.objects.all()
    visit_counter = Count.objects.get(name="Actual")
    visit_add = Count.objects.get(name="Extra")
    count_list = str(visit_counter.count + visit_add.count)
    count = list(count_list)
    pg = Programme.objects.all()
    return render(request,'404.html', {'pg': pg, 'count': count, 'events' : events})

def mentors(request):
    events = Event.objects.all()
    visit_counter = Count.objects.get(name="Actual")
    visit_add = Count.objects.get(name="Extra")
    count_list = str(visit_counter.count + visit_add.count)
    count = list(count_list)
    pg = Programme.objects.all()
    mentor_type = Mentor_type.objects.all()
    return render(request,'mentors.html', {'mentor_type': mentor_type, 'pg': pg, 'count': count, 'events' : events})

def cabinspace(request):
    events = Event.objects.all()
    visit_counter = Count.objects.get(name="Actual")
    visit_add = Count.objects.get(name="Extra")
    count_list = str(visit_counter.count + visit_add.count)
    count = list(count_list)
    pg = Programme.objects.all()
    return render(request,'cabinspace.html', {'pg': pg, 'count': count, 'events' : events})

def iot(request):
    events = Event.objects.all()
    visit_counter = Count.objects.get(name="Actual")
    visit_add = Count.objects.get(name="Extra")
    count_list = str(visit_counter.count + visit_add.count)
    count = list(count_list)
    devices = IotDevice.objects.all()
    specs = []
    temp=  []
    for i in devices:
        temp = i.desc.split("\n")
        others = [j.split(":") for j in temp]
        specs.append(others)
    print(specs)
    pg = Programme.objects.all()
    return render(request,'iot.html', {'pg': pg, 'count': count, 'devices': devices, 'events' : events, 'specs': specs})    

def labs(request):
    events = Event.objects.all()
    visit_counter = Count.objects.get(name="Actual")
    visit_add = Count.objects.get(name="Extra")
    count_list = str(visit_counter.count + visit_add.count)
    count = list(count_list)
    pg = Programme.objects.all()
    return render(request,'labs.html', {'pg': pg, 'count': count, 'events' : events})

def loginuser(request):
    events = Event.objects.all()
    visit_counter = Count.objects.get(name="Actual")
    visit_add = Count.objects.get(name="Extra")
    count_list = str(visit_counter.count + visit_add.count)
    count = list(count_list)
    pg = Programme.objects.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        try:
            user = User.objects.get(email=email)
            print(user)
            print(user.password)
            if user.password == password:
                login(request,user)
                return redirect('booking')
            else:
                return render(request,'login.html',{'error':'Invalid Credentials', 'pg': pg, 'count': count, 'events': events})
        except:
            return render(request,'login.html',{'error':'Invalid Credentials', 'pg': pg, 'count': count, 'events': events})
    return render(request,'login.html', {'pg': pg, 'count': count, 'events': events})

def logoutuser(request):
    logout(request)
    return redirect('index')