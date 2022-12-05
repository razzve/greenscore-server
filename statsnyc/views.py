from django.shortcuts import render
#importing tables
from .models import Greeninfra, Energy
#connection for raw sql queries to the db
from django.db import connection, transaction
from django.db.models import F

from django.http import HttpResponse
from .place_to_geocode import geocode

from .getAqi import getAqi
import numpy as np

import statistics

def distance(lat1, lon1, lat2, lon2, r=3956):
    	# Convert degrees to radians
		coordinates = lat1, lon1, lat2, lon2
    	# radians(c) is same as c*pi/180
		phi1, lambda1, phi2, lambda2 = [np.radians(c) for c in coordinates]  
    
    	# Apply the haversine formula
		a = (np.square(np.sin((phi2-phi1)/2)) + np.cos(phi1) * np.cos(phi2) * np.square(np.sin((lambda2-lambda1)/2)))
		d = 2*r*np.arcsin(np.sqrt(a))
		return d

#getAirq accepts an http request with a place GET parameter 
#returns an http response with all the air quality metrics for it
#def getAirq(lng, lat):
# return first AQI from database using longitude, latitide
#	for obj in Airq.objects.all():
#		if (obj.latitude_sw <= lat <= obj.latitude_ne) and \
#			(obj.longitude_sw <= lng <= obj.longitude_ne):
#			aqi = obj.aqi
#			return HttpResponse(aqi)
#	return HttpResponse("ERROR: 404 Not Found.")

#return averge energy score from database using longitude, latitude
def getEnergy(lng, lat):
	values = []
	for obj in Energy.objects.all()[1:]:
		if (obj.lat and obj.lng):
			if distance(float(lat), float(lng), float(obj.lat), float(obj.lng)) < 5: # area threshold (0.1) for consideration
				if obj.score != 'Not Available':
					values.append(int(obj.score))

	energy = sum(values) // len(values)
	return energy


def calcAQI(request):
	for obj in Airq.objects.all():
		the_aqi = 1 #this would be the aqi
		obj.aqi = the_aqi
		obj.save()


#getGreeninfra accepts an http request with longitude and latitude parameters
#returns an http response with the green infrastructure metrics for the coordinates
def getGreeninfra(lng, lat):
	# def dist_away(lngA, latA, lngB, latB):
	# 	a = ((math.sin((latB - latA)/2))**2) + math.cos(latA) * math.cos(latB) * ((math.sin((lngB - lngA)/2))**2)
	# 	return 2 * 3956 * math.asin(math.sqrt(a))

	greenarea_total = []

	# dist_away(float(lng), float(lat), float(obj.longitude), float(obj.latitude)) 
	for obj in Greeninfra.objects.all()[1:]:
		if (obj.latitude and obj.longitude):
			if distance(float(lat), float(lng), float(obj.latitude), float(obj.longitude)) < 5: # area threshold (0.1) for consideration
				greenarea_total.append(float(obj.area)) 

	return sum(greenarea_total)

# calculate final greenscore using geolocation
def getGreenScore(request):
	lng = request.GET.get("lng", None)
	lat = request.GET.get("lat", None)
	assert (None not in [lng, lat])
	energy = getEnergy(lng, lat) # get energy
	airq = getAqi()
	infra = getGreeninfra(lng, lat)
	greenscore = (energy + airq + infra) // 3
	return HttpResponse() 

def greenscore(request):
	lng = request.GET.get("lng", None)
	lat = request.GET.get("lat", None)
	assert (None not in [lng, lat])
	energy = getEnergy(lng, lat)
	airq = getAqi()

	sumareas = []
	for obj in Greeninfra.objects.all():
		sumareas.append(obj.area)

	avgareas = sum (sumareas) // len(sumareas)	 
	stdareas = statistics.stdev(sumareas)
	
	infra = getGreeninfra(lng, lat)
	normalizedinfra = (infra-avgareas)/stdareas

	greenscore = (energy + airq + normalizedinfra) // 3
	#MinMax Way
	#normalizedgs = ((rawgs-min(totalgreenscores))*500)/(max(totalgreenscores)-min(totalgreenscores))
	#Z-Score Way
	#normalizedgs = (rawgs-mean(totalgreenscores))/std(totalgreenscores)
	return HttpResponse((greenscore)/175)