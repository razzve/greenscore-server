from django.shortcuts import render
#importing tables
from .models import Airq, Greeninfra
#connection for raw sql queries to the db
from django.db import connection, transaction
from django.db.models import F

from django.http import HttpResponse
from .place_to_geocode import geocode

#getAirq accepts an http request with a place GET parameter 
#returns an http response with all the air quality metrics for it
def getAirq(request):
	place = request.GET.get('place', '')
	result = Airq.objects.filter(geo_place = place)

	#for obj in Airq.objects.all():
	#	pl = obj.geo_place
	#
	#	gcode = geocode(pl)
	#	obj.latitude_ne = gcode[0][0]
	#	obj.longitude_ne = gcode[0][1]
	#	obj.latitude_sw = gcode[1][0]
	#	obj.longitude_sw= gcode[1][1]	
	#	obj.save()

	


	return HttpResponse(result.values())

def calcAQI(request):
	for obj in Airq.objects.all():
		the_aqi = 1 #this would be the aqi
		obj.aqi = the_aqi
		obj.save()



#getGreeninfra accepts an http request with longitude and latitude parameters
#returns an http response with the green infrastructure metrics for the coordinates
def getGreeninfra(request):
	lat = request.GET.get('lat','')
	lng = request.GET.get('lng', '')
	result = Greeninfra.objects.filter(latitude = lat, longitude = lng)

	return HttpResponse(result.values())