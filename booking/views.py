import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import aTimeSlot
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
from django.core.paginator import Paginator
from django.db.models import F
import xlsxwriter
from mainsite.models import *

# Create your views here.
User = get_user_model()

def index(request):
    visit_counter = Count.objects.get(name="Actual")
    visit_add = Count.objects.get(name="Extra")
    
    count_list = str(visit_counter.count + visit_add.count)
    count = list(count_list)
    pg = Programme.objects.all()
    # list of times from 9am to 9pm in intervals of 30 mins
    times = ["09.00 am", "09.30 am", "10.00 am", "10.30 am", "11.00 am", "11.30 am", "12.00 pm", "12.30 pm", "01.00 pm", "01.30 pm", "02.00 pm", "02.30 pm",
             "03.00 pm", "03.30 pm", "04.00 pm", "04.30 pm", "05.00 pm", "05.30 pm", "06.00 pm", "06.30 pm", "07.00 pm", "07.30 pm", "08.00 pm", "08.30 pm"]
    date = datetime.now().strftime("%Y-%m-%d")
    status = 0
    user = request.user
    if user.is_authenticated:
        status = User.objects.get(email=user.email).lock
    if request.method == "POST":
        if 'form1' in request.POST:
            date = request.POST.get("dateinput")
            print(date)
        elif 'form2' in request.POST:
            user = request.user
            if not user.is_authenticated:
                return redirect("login")
            selected_ids = request.POST.get('selected_ids')
            if selected_ids == "":
                return redirect('index')
            l = selected_ids.split(",")
            room = 0
            date = request.POST.get('dateinput')
            name = request.POST.get('name')
            month = request.POST.get('month')
            year = request.POST.get('year')
            reason = request.POST.get('reason')
            u = User.objects.get(email=user.email)
            print(u)
            for i in l:
                j = i.split("-")
                slot = j[1]
                room = int(j[2])
                print(slot, room, date)
                b = aTimeSlot.objects.filter(slot=slot, room=room, date=date)
                if b:
                    continue
                else:
                    x = aTimeSlot.objects.create(
                        slot=slot, room=room, date=date, name=name, email=user.email, month=month, year=year, reason=reason)
                    u.free_slots += 0.5
                    x.save()
                    u.save()
            if u.free_slots > u.total:
                u.lock = 1
                u.save()
        elif 'form4' in request.POST:
            date = request.POST.get("dateinput")
    timeslots = aTimeSlot.objects.filter(date=date)
    num = range(24)
    r = range(3)
    return render(request, 'booking.html', {'timeslots': timeslots, 'num': num, 'r': r, 'date': date, 'times': times, 'status': status, 'pg': pg, 'count': count})


def delete_slot(request):
    visit_counter = Count.objects.get(name="Actual")
    visit_add = Count.objects.get(name="Extra")
    
    count_list = str(visit_counter.count + visit_add.count)
    count = list(count_list)
    pg = Programme.objects.all()
    times = ["09.00 am", "09.30 am", "10.00 am", "10.30 am", "11.00 am", "11.30 am", "12.00 pm", "12.30 pm", "01.00 pm", "01.30 pm", "02.00 pm", "02.30 pm",
             "03.00 pm", "03.30 pm", "04.00 pm", "04.30 pm", "05.00 pm", "05.30 pm", "06.00 pm", "06.30 pm", "07.00 pm", "07.30 pm", "08.00 pm", "08.30 pm"]
    date = datetime.now().strftime("%Y-%m-%d")
    if request.method == "POST":
        if 'form1' in request.POST:
            date = request.POST.get("dateinput")
            print(date)
        elif 'form2' in request.POST:
            user = request.user
            if not user.is_authenticated:
                return redirect("login")
            selected_ids = request.POST.get('selected_ids')
            if selected_ids == "":
                return redirect('index')
            l = selected_ids.split(",")
            room = 0
            date = request.POST.get('dateinput')
            u = User.objects.get(email=user.email)
            for i in l:
                j = i.split("-")
                slot = j[1]
                room = int(j[2])
                a = aTimeSlot.objects.filter(slot=slot, room=room, date=date)
                a.delete()
                u.free_slots += 0.5
                u.charges = u.free_slots * -300 if u.free_slots < 0 else 0
    timeslots = aTimeSlot.objects.filter(date=date)
    num = range(24)
    r = range(3)
    return render(request, 'deletecal.html', {'timeslots': timeslots, 'num': num, 'r': r, 'date': date, 'times': times, 'pg': pg, 'count': count})


def profile(request):
    visit_counter = Count.objects.get(name="Actual")
    visit_add = Count.objects.get(name="Extra")
    
    count_list = str(visit_counter.count + visit_add.count)
    count = list(count_list)
    pg = Programme.objects.all()
    mon = datetime.now().strftime("%Y-%m-%d").split("-")[1]
    y = datetime.now().strftime("%Y-%m-%d").split("-")[0]
    objs = User.objects.filter(is_superuser=False)
    print(objs)
    for o in objs:
        o.free_slots = aTimeSlot.objects.filter(
            email=o.email, month=mon, year=y).count()*0.5
        o.charges = 0 if o.free_slots < o.total else (o.free_slots - o.total) * 300
        o.save()
    if request.method == "POST":
        if 'form1' in request.POST:
            email = request.POST.get("email")
            return redirect(reverse('edit_user') + f'?email={email}')
        elif 'form2' in request.POST:
            return redirect('change_password')
        elif 'form4' in request.POST:
            email = request.POST.get("email")
            u = User.objects.get(email=email)
            u.lock = int(request.POST.get("lock"))
            u.save()
    user = request.user
    free_hours = User.objects.get(email=user.email).free_slots
    charges = User.objects.get(email=user.email).charges
    total = User.objects.get(email=user.email).total
    # objs = User.objects.all()
    date = datetime.now().strftime("%Y-%m-%d")
    month = date.split("-")[1]
    year = date.split("-")[0]
    if month == "01":
        previous_month = "12"
        # Subtract 1 from the year for January
        previous_year = str(int(year) - 1)
    else:
        previous_month = str(int(month) - 1).zfill(2)
        previous_year = year
    print(month, year)
    timeslots_tm = aTimeSlot.objects.filter(
        email=user.email, month=month, year=year)
    timeslots = sorted(timeslots_tm, key=lambda obj: obj.date)
    timeslots_pm = aTimeSlot.objects.filter(
        email=user.email, month=previous_month, year=previous_year)
    timeslotspm = sorted(timeslots_pm, key=lambda obj: obj.date)
    timeslots.extend(timeslotspm)
    per_page = 10

    paginator = Paginator(timeslots, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    logs = page_obj.object_list
    if not user.is_authenticated:
        return redirect("login")
    return render(request, 'profile.html', {'logs': logs, 'page_obj': page_obj, 'free_hours': free_hours, 'charges': charges, "objs": objs, 'total': total, 'pg': pg, 'count': count})


def edit_user(request):
    visit_counter = Count.objects.get(name="Actual")
    visit_add = Count.objects.get(name="Extra")
    
    count_list = str(visit_counter.count + visit_add.count)
    count = list(count_list)
    pg = Programme.objects.all()
    email = request.GET.get('email')
    u = User.objects.get(email=email)
    x = u.total
    us = User.objects.get(email=email)
    if request.method == "POST":
        if 'form1' in request.POST:
            first_name = request.POST.get('first_name')
            email = request.POST.get("email")
            free = request.POST.get("free")
            u.company_name = first_name
            u.email = email
            u.total = free
            u.save()
            return redirect('profile')
        else:
            print('Hello')
            email = request.POST.get('email')
            us = User.objects.get(email=email)
            a = aTimeSlot.objects.filter(email=email)
            u = User.objects.get(email=email)
            us.delete()
            u.delete()
            a.delete()
            return redirect('profile')
    return render(request, 'edituser.html', {'x': x, 'us': us, 'pg': pg, 'count': count})


def change_password(request):
    visit_counter = Count.objects.get(name="Actual")
    visit_add = Count.objects.get(name="Extra")
    
    count_list = str(visit_counter.count + visit_add.count)
    count = list(count_list)
    pg = Programme.objects.all()
    if request.method == "POST":
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        if password == confirmpassword:
            user = request.user
            user.password = password
            user.save()
            login(request, user)
            return redirect('profile')
        return render(request, 'changepassword.html', {'error': 'Passwords do not match', 'pg': pg, 'count': count})
    return render(request, 'changepassword.html', {'pg': pg, 'count': count})


def download_table_as_excel(request):
    objs = User.objects.all()

    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Charges.xlsx"'

    workbook = xlsxwriter.Workbook(response, {'remove_timezone': True})
    worksheet = workbook.add_worksheet()

    # Write the table headers
    headers = ['Company Name', 'Email',
               'Hours Used', 'Total Free Hours', 'Charges']
    for col, header in enumerate(headers):
        worksheet.write(0, col, header)

    # Write the table data
    for row, obj in enumerate(objs, start=1):
        data = [obj.company_name, obj.email,
                obj.free_slots, obj.total, str(obj.charges)+'0']
        for col, value in enumerate(data):
            worksheet.write(row, col, value)

    workbook.close()

    return response

