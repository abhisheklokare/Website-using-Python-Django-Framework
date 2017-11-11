from django.shortcuts import render, redirect
from django.views import generic
from .models import Customer
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from .forms import CustomerForm
from django.views.generic.edit import CreateView
from . import forms
from pytz import timezone
from django.core.mail import send_mail

class BaseView(generic.DetailView):
    model = Customer
    template_name='website/base.html'

def homeView(request):
    template = loader.get_template('website/index.html')
    return HttpResponse(template.render(None,request))

def aboutusView(request):
    template = loader.get_template('website/aboutus.html')
    return HttpResponse(template.render(None,request))

def galleryView(request):
    template = loader.get_template('website/gallery.html')
    return HttpResponse(template.render(None,request))

def contactusView(request):
    template = loader.get_template('website/contactus.html')
    return HttpResponse(template.render(None,request))

def contactusView(request):
    if request.method == "GET" :
        form = CustomerForm()
    else :
        form = CustomerForm(request.POST)
        customer = Customer()
        customer.name = request.POST.get("name")
        customer.email = request.POST.get("email")
        customer.mobileNum = request.POST.get("mobileNum")
        customer.roofType = request.POST.get("roofType")
        customer.roofHeight = request.POST.get("roofHeight")
        customer.electricityBoard = request.POST.get("electricityBoard")
        customer.otherDetails = request.POST.get("otherDetails")
        customer.address = request.POST.get("address")
        customer.latitude = request.POST.get("latitude")
        customer.longitude = request.POST.get("longitude")
        customer.save()
        message = 'Name : {name} \nEmail : {email} \nMobile : {mob} \nRoof Type : {roofType} \nRoof Height : {roofHeight} \nElectricity Board : {eboard} \nOther Details : {details} \nAddress : {addr} \nLatitide : {lat} \nLongitude : {lon}'.format(name=customer.name, email=customer.email, mob=customer.mobileNum, roofType=customer.roofType, roofHeight=customer.roofHeight, eboard=customer.electricityBoard, details=customer.otherDetails, addr=customer.address, lat=customer.latitude, lon=customer.longitude,)
        send_mail(customer.name + ' has sent you a query!!!' , message, 'amitm20692@gmail.com', ['abhi.rocks1289@gmail.com','amitm20692@gmail.com'], fail_silently=False,)
        return render(request, "website/index.html", {'success_status' : "success", 'contact_name' : request.POST.get("name")})
    return render(request, "website/contact.html", {'form': form})
