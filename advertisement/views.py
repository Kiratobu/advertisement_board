from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from advertisement.models import Advertisement
from django.views import View,generic




def advertisement_list(request,*args, **kwargs):
    advertisements = Advertisement.objects.all()
    return render(request,'advertisement/advertisement_list.html',{'advertisements': advertisements})



class Country(View):
    
    def get(self, request):
        return render(request,'advertisement/country.html',{})
    
    def post(self, request):
        return render(request,'advertisement/contacts.html',{})



class AdvertisementListView(generic.ListView):
    model = Advertisement
    template_name = 'advertisement_list.html'
    context_object_name = 'advertisement_list'
    queryset = Advertisement.objects.all()


class AdvertisementDetailView(generic.DetailView):
    model = Advertisement