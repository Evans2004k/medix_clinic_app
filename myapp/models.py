from django.db import models


class Appointment(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    date = models.DateField()
    message = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.fullName} - {self.department}"


# Backwards-compatible name for existing code.
appointment = Appointment


class ContactMessage(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=15, blank=True)
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.subject} - {self.fullName}"