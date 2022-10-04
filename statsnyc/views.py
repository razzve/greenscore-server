from django.shortcuts import render
#importing tables
from .models import Airq, Greeninfra
#connection for raw sql queries to the db
from django.db import connection, transaction
from django.http import HttpResponse

#getAirq accepts an http request with a place GET parameter 
#returns an http response with all the air quality metrics for it
def getAirq(request):
	place = request.GET.get('place', '')
	result = Airq.objects.filter(geo_place = place)

	return HttpResponse(result.values())

#getGreeninfra accepts an http request with longitude and latitude parameters
#returns an http response with the green infrastructure metrics for the coordinates
def getGreeninfra(request):
	lat = request.GET.get('lat','')
	lng = request.GET.get('lng', '')
	result = Greeninfra.objects.filter(latitude = lat, longitude = lng)

	return HttpResponse(result.values())