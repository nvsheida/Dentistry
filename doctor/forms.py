from django import forms
from .models import Appointment, Dentist, Contact


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['first_name', 'last_name', 'email', 'phone', 'dentist','dentist_time']

    def clean(self):
        cleaned_data = super().clean()
        dentist_time= cleaned_data.get('dentist_time')

        if dentist_time:
            existing_appointment = Appointment.objects.filter(dentist_time).exists()
            if existing_appointment:
                raise forms.ValidationError("این نوبت انتخاب شده است لطفا یک ساعت دیگر انتخاب کنید")
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dentist'].queryset = Dentist.objects.all()


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name','email','message']