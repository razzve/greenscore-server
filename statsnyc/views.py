from django.shortcuts import render
#importing tables
from .models import Airq, Greeninfra, Energy
#connection for raw sql queries to the db
from django.db import connection, transaction
from django.db.models import F

from django.http import HttpResponse
from .place_to_geocode import geocode

import math

#getAirq accepts an http request with a place GET parameter 
#returns an http response with all the air quality metrics for it
def getAirq(lng, lat):
# return first AQI from database using longitude, latitide
	for obj in Airq.objects.all():
		if (obj.latitude_sw <= lat <= obj.latitude_ne) and \
			(obj.longitude_sw <= lng <= obj.longitude_ne):
			aqi = obj.aqi
			return HttpResponse(aqi)
	return HttpResponse("ERROR: 404 Not Found.")

#return averge energy score from database using longitude, latitude
def getEnergy(request):
	def dist_away(lngA, latA, lngB, latB):
		a = (math.sin((latB - latA)/2))**2 + math.cos(latA) * math.cos(latB) * (math.sin((lngB - lngA)/2))**2
		return 2 * 3956 * math.asin(a)

	lng = request.GET.get("lng", None)
	lat = request.GET.get("lat", None)
	values = []
	for obj in Energy.objects.all():
		if dist_away(lng, lat, obj.lng, obj.lat) < 0.5: # area threshold (0.1) for consideration
			values.append(obj.score)
	energy = sum(values) // len(values)
	return HttpResponse(energy)


def calcAQI(request):
	for obj in Airq.objects.all():
		the_aqi = 1 #this would be the aqi
		obj.aqi = the_aqi
		obj.save()


#getGreeninfra accepts an http request with longitude and latitude parameters
#returns an http response with the green infrastructure metrics for the coordinates
def getGreeninfra(request):
	lng = request.GET.get("lng", None)
	lat = request.GET.get("lat", None)
	def dist_away(lngA, latA, lngB, latB):
		a = (math.sin((latB - latA)/2))**2 + math.cos(latA) * math.cos(latB) * (math.sin((lngB - lngA)/2))**2
		return 2 * 3956 * math.asin(a)
	
	greenarea_total = 0
	
	for obj in Greeninfra.objects.all():
		if dist_away(float(lng), float(lat), float(obj.longitude), float(obj.latitude)) < 0.5:
			greenarea_total += obj.area
	return HttpResponse(greenarea_total)

# calculate final greenscore using geolocation
def getGreenScore(request):
	lng = request.GET.get("lng", None)
	lat = request.GET.get("lat", None)
	assert (None not in [lng, lat])
	energy = getEnergy(lng, lat) # get energy
	airq = getAirq(lng, lat)
	infra = getGreeninfra(lng, lat)
	greenscore = (energy + airq + infra) // 3
	return HttpResponse() 