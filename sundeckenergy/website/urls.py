from django.conf.urls import url
from . import views

app_name = 'website'
urlpatterns = [
    #contactus/
    url(r'^$', views.homeView, name='home_view'),
    url(r'^about-us/$', views.aboutusView, name='about_view'),
    url(r'^gallery/$', views.galleryView, name='gallery_view'),
    url(r'^contact-us/$', views.contactusView, name='contact_view'),
]
