from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from doctor.forms import AppointmentForm, ContactForm
from doctor.models import Dentist, DentistTime, Appointment
from django.contrib import messages


def home_view(request):
    return render(request, 'test.html')


def dentists_view(request):
    return render(request, 'dentists.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            message_name = contact.first_name
            message_email = contact.email
            message = contact.message
            send_mail(
                message_name,
                message,
                message_email,
                ['sheida.alikhani1381@gmail.com']
            )
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


@login_required
def booking_view(request):
    global dentists, denttimes
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            existing_appointment = Appointment.objects.filter(dentist_id=appointment.dentist_id,
                                                              dentist_time=appointment.dentist_time)
            if existing_appointment.exists():
                messages.error(request, "این نوبت رزرو شده است لطفا یک نوبت دیگر انتخاب کنید")
                return redirect('home')
            appointment.save()
            messages.success(request, 'نوبت شما با موفقیت ثبت شد')
            return redirect('home')
    else:
        if 'dentist_id' in request.GET:
            selected_doctor_id = int(request.GET.get('dentist_id'))
            denttimes = DentistTime.objects.filter(dentist_id=selected_doctor_id)
        else:
            denttimes = DentistTime.objects.all()
        dentists = Dentist.objects.all().order_by('full_name')
        form = AppointmentForm()
    return render(request, 'booking.html', {'form': form, 'dentists': dentists,
                                            'denttimes': denttimes})
