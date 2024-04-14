"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('cart', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('faq', views.faq, name="faq"),
    path('gallery', views.gallery, name="gallery"),
    path('gallerycarousel', views.gallerycarousel, name="gallerycarousel"),
    path('news', views.news, name="news"),
    path('newsdetails', views.newsdetails, name="newsdetails"),
    path('newscarousel', views.newscarousel, name="newscarousel"),
    path('newssidebar', views.newssidebar, name="newssidebar"),
    path('newssidebarleft', views.newssidebarleft, name="newssidebarleft"),
    path('packages1', views.packages1, name="packages1"),
    path('packages2', views.packages2, name="packages2"),
    path('products', views.products, name="products"),
    path('productdetails', views.productdetails, name="productdetails"),
    path('services', views.services, name="services"),
    path('servicescarousel', views.servicescarousel, name="servicescarousel"),
    path('team', views.team, name="team"),
    path('teamcarousel', views.teamcarousel, name="teamcarousel"),
    path('testimonials', views.testimonials, name="testimonials"),
]