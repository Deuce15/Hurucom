import os

from flask import Flask, request, redirect, url_for
from flask_mail import Mail, Message

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def cart(request):
    return render(request, 'cart.html', {})

def checkout(request):
    return render(request, 'checkout.html', {})

def faq(request):
    return render(request, 'faq.html', {})

def gallery(request):
    return render(request, 'gallery.html', {})

def gallerycarousel(request):
    return render(request, 'gallery-carousel.html', {})

def news(request):
    return render(request, 'news.html', {})

def newsdetails(request):
    return render(request, 'news-details.html', {})

def newscarousel(request):
    return render(request, 'news-carousel.html', {})

def newssidebar(request):
    return render(request, 'news-sidebar.html', {})

def newssidebarleft(request):
    return render(request, 'news-sidebar-left.html', {})

def packages1(request):
    return render(request, 'packages-01.html', {})


def packages2(request):
    return render(request, 'packages-02.html', {})

def team(request):
    return render(request, 'team.html', {})

def teamcarousel(request):
    return render(request, 'team-carousel.html', {})

def products(request):
    return render(request, 'products.html', {})

def productdetails(request):
    return render(request, 'product-details.html', {})

def services(request):
    return render(request, 'services.html', {})

def servicescarousel(request):
    return render(request, 'services-carousel.html', {})

def testimonials(request):
    return render(request, 'testimonials.html', {})

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['i.nyamu5@gmail.com']
    message = Message('Subscription Confirmation', sender='sender@example.com', recipients=[email])
    message.body = 'Thank you for subscribing to our newsletter!'
    mail.send(message)
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return '<h1>Subscription successful!</h1>'

if __name__ == '__main__':
    app.run(debug=True)