from django.db import models
from users.models import User


class Dentist(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)


class DentistTime(models.Model):
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    dentist_date = models.DateTimeField(null=False, blank=False)
    dentist_time = models.TimeField(null=False, blank=False)


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    dentist_time = models.ForeignKey(DentistTime, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    date = models.DateTimeField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)

    class Meta:
        unique_together = (('dentist', 'dentist_time'),)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()