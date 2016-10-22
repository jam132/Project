from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import UserForm, ProfileForm
from .models import Profile
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.template import RequestContext
from .forms import BookingForm, ViewBookingsForm
from .models import Booking, Doctor
from django.core.mail import EmailMessage
from datetime import timedelta
import datetime


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def staff(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    elif request.user.is_staff and not request.user.is_superuser:
        email = request.user.email
        hall_staff = Doctor.objects.get(doctor_admin=email)
        stf = Booking.objects.filter(Q(date=datetime.date.today(), start_time__gte=datetime.datetime.now(). \
                                       strftime('%I:%M %p')) | Q(date__gt=datetime.date.today()), doctor=hall_staff).order_by(
            '-date', 'start_time')
        return render(request, "reservations/staff.html", {"staff": stf})
    else:
        return HttpResponseRedirect('/')

        

def book(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.user.is_staff or request.user.is_superuser:
        return HttpResponseRedirect('/')
    elif request.user.is_authenticated():
        if request.method == 'POST':
            form = BookingForm(request.POST)
            name = request.POST['name']
            book_doc = request.POST['doctor']

            if form.is_valid():
                value = form.save(commit=False)
                user = User.objects.all()
                value.email = request.user.email
                value.save()

                # Getting hall admin email_id such that the email can be forwarded to the hall_admin.
                email = Doctor.objects.filter(id=book_doc).values('doctor_admin')

                # Sending email to the hall_admin containing event info and user email.
                # user_email = EmailMessage('Booking System', 'Please accept the request for booking', to=[email])
                # user_email.send()
                return render(request, "reservations/thanks.html", {})
        else:
            form = BookingForm()
        return render(request, "reservations/book.html", {"form": form})
    

def view(request):
    if request.method == 'POST':
        form = ViewBookingsForm(request.POST)
        view_doc = request.POST['doctor']
        view_date = request.POST['date']
        if form.is_valid():
            boo = Booking.objects.filter( doctor=view_doc, date=view_date)
            return render(request, "reservations/view_booking.html", {"booking": boo, "view": view, })
    else:
        form = ViewBookingsForm()
    return render(request, "reservations/view.html", {"form": form})


def update_profile(request, user_id):
    instance = get_object_or_404(Profile, pk=user_id)
    form = ProfileForm(request.POST or None,request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #messages.success(request, "Changes saved")
        user = request.user
        profile = get_object_or_404(Profile, pk=user_id)
        return render(request, 'login/detail.html', {'profile': profile, 'user': user})
    context = {
		"profile": instance,
		"form":form,
	}
    return render(request, 'login/create_profile.html', context)

def create_profile(request):
    if not request.user.is_authenticated():
        return render(request, 'login/login.html')
    else:
        form = ProfileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.id = profile.user_id
            profile.create = True
            profile.profile_pic = request.FILES['profile_pic']
            file_type = profile.profile_pic.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'profile': profile,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'login/create_profile.html', context)
            profile.save()
            return render(request, 'login/detail.html', {'profile': profile})
        context = {
            "form": form,
        }
        return render(request, 'login/create_profile.html', context)

def detail(request, user_id):
    if not request.user.is_authenticated():
        return render(request, 'login/login.html')
    else:
        user = request.user
        profile = get_object_or_404(Profile, pk=user_id)
        return render(request, 'login/detail.html', {'profile': profile, 'user': user})

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'login/login.html')
    else:
        return render(request, 'login/index.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'login/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'login/index.html')
            else:
                return render(request, 'login/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login/login.html', {'error_message': 'Invalid login'})
    return render(request, 'login/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'login/index.html')
    context = {
        "form": form,
    }
    return render(request, 'login/register.html', context)

