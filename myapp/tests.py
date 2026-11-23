from django.test import TestCase
from django.urls import reverse
from .models import Appointment, ContactMessage


class AppointmentTests(TestCase):
    def test_valid_appointment_is_saved(self):
        response = self.client.post(
            reverse("appointment"),
            {
                "fullName": "John Doe",
                "email": "john@example.com",
                "phoneNumber": "1234567890",
                "department": "Cardiology",
                "date": "2026-12-01",
                "message": "Test symptoms",
            },
        )

        self.assertRedirects(response, reverse("appointment"))
        self.assertTrue(Appointment.objects.filter(email="john@example.com").exists())

    def test_invalid_appointment_is_not_saved(self):
        response = self.client.post(reverse("appointment"), {"email": "invalid"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Appointment.objects.count(), 0)


class ContactFormTests(TestCase):
    def test_valid_contact_message_is_saved(self):
        response = self.client.post(
            reverse("contact"),
            {
                "fullName": "Jane Doe",
                "email": "jane@example.com",
                "phoneNumber": "",
                "subject": "Clinic hours",
                "message": "What time do you open?",
            },
        )

        self.assertRedirects(response, reverse("contact"))
        self.assertTrue(
            ContactMessage.objects.filter(
                email="jane@example.com",
                subject="Clinic hours",
            ).exists()
        )

    def test_invalid_contact_message_is_not_saved(self):
        response = self.client.post(
            reverse("contact"),
            {
                "fullName": "Jane Doe",
                "email": "not-an-email",
                "subject": "",
                "message": "A message",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter a valid email address")
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_contact_page_renders_form(self):
        response = self.client.get(reverse("contact"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name="subject"')
        self.assertContains(response, 'name="phoneNumber"')
