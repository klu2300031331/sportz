from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactUs  # Assuming you have a model to store contact information




def contactlogic(request):
    if request.method == "POST":
        # Retrieve form data from POST request
        full_name = request.POST['full-name']
        email = request.POST['email']
        message = request.POST['message']

        # Save contact data into the database (optional)
        contact_data = ContactUs(full_name=full_name, email=email, message=message)
        contact_data.save()

        # Prepare the email
        subject = f"Contact Form Submission from {full_name}"
        message_body = f"Message: {message}\n\nFrom: {full_name}\nEmail: {email}"

        # Send email to the designated email address from settings.py
        send_mail(
            subject,
            message_body,
            settings.DEFAULT_FROM_EMAIL,  # This is the email set in your settings.py
            [settings.CONTACT_EMAIL],  # This should be the email address to receive contact form messages
            fail_silently=False,
        )

        # Send a thank you response to the user
        return HttpResponse("<h1><center>Thank you for reaching out! We will get back to you soon.</center></h1>")

    return HttpResponse("<h1><center>Error: Invalid request.</center></h1>")


def contact_us(request):
    return render(request,'contact_us.html')
