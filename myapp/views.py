from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AppointmentForm, ContactForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def departments(request):
    return render(request, 'departments (1).html')

def department_details(request):
    return render(request, 'department-details (1).html')

def services(request):
    return render(request, 'services (1).html')

def service_details(request):
    return render(request, 'service-details (1).html')

def doctors(request):
    return render(request, 'doctors (1).html')

def appointment(request):
    form = AppointmentForm(
        request.POST if request.method == "POST" else None
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Your appointment has been scheduled. Thank you!")
        return redirect("appointment")

    return render(
        request,
        "appointment (1).html",
        {"form": form},
    )

def testimonials(request):
    return render(request, 'testimonials.html')

def faq(request):
    return render(request, 'faq (1).html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    form = ContactForm(
        request.POST if request.method == "POST" else None
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Your message has been sent. Thank you!")
        return redirect("contact")

    return render(
        request,
        "contact.html",
        {"form": form},
    )

def terms(request):
    return render(request, 'terms (1).html')

def privacy(request):
    return render(request, 'privacy (1).html')

def starter(request):
    return render(request, 'starter-page (1).html')

def not_found(request, exception=None):
    return render(request, '404 (1).html', status=404)