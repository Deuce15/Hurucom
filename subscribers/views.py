from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriberForm  # Make sure you have this form defined
from .models import Subscriber  # Ensure the Subscriber model is defined

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            subscriber = form.save()
            try:
                send_mail(
                    'Subscription Confirmation',
                    'Thank you for subscribing to our newsletter!',
                    settings.EMAIL_HOST_USER,
                    [subscriber.email],
                    fail_silently=False,
                )
                messages.success(request, 'Subscription successful! A confirmation email has been sent.')
            except Exception as e:
                messages.error(request, f'Subscription successful, but an error occurred while sending the email: {e}')
            return redirect('subscribe')
        else:
            messages.error(request, 'Subscription failed. Please try again.')
    else:
        form = SubscriberForm()
    return render(request, 'subscribers/subscribe.html', {'form': form})

def send_test_email(request):
    try:
        send_mail(
            'Test Email Subject',
            'This is a test email body.',
            settings.EMAIL_HOST_USER,  # Ensure this is set in your settings.py
            ['i.nyamu5@gmail.com'],
            fail_silently=False,
        )
        return HttpResponse("Email sent successfully")
    except Exception as e:
        return HttpResponse(f"Failed to send email: {e}")

