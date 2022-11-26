from django.shortcuts import render
#importing tables
from .models import Airq, Greeninfra, Energy
#connection for raw sql queries to the db
from django.db import connection, transaction
from django.db.models import F

from django.http import HttpResponse
from .place_to_geocode import geocode

#getAirq accepts an http request with a place GET parameter 
#returns an http response with all the air quality metrics for it
def getAirq(lng, lat):
# return first AQI from database using longitude, latitide
	for obj in Airq.objects.all():
		if (obj.latitude_sw <= lat <= obj.latitude_ne) and \
			(obj.longitude_sw <= lng <= obj.longitude_ne):
			return obj.aqi
	return HttpResponse("ERROR: 404 Not Found.")


	# place = request.GET.get('place', '')
	# result = Airq.objects.filter(geo_place = place)
	
	#for obj in Airq.objects.all():
	#	pl = obj.geo_place
	#
	#	gcode = geocode(pl)
	#	obj.latitude_ne = gcode[0][0]
	#	obj.longitude_ne = gcode[0][1]
	#	obj.latitude_sw = gcode[1][0]
	#	obj.longitude_sw= gcode[1][1]	
	#	obj.save()

	#return HttpResponse(result.values())

#return averge energy score from database using longitude, latitude
def getEnergy(lng, lat):
	# lng = request.GET.get("lng", None)
	# lat = request.GET.get("lat", None)
	values = []
	for obj in Energy.objects.all():
		if isinstance(obj.score, int):
			if (abs(lng - obj.lng) < 0.1 and abs(lat - obj.lng) < 0.1): # area threshold (0.1) for consideration
				values.append(obj.score)
	avg = avg(values)
	return avg


def calcAQI(request):
	for obj in Airq.objects.all():
		the_aqi = 1 #this would be the aqi
		obj.aqi = the_aqi
		obj.save()


#getGreeninfra accepts an http request with longitude and latitude parameters
#returns an http response with the green infrastructure metrics for the coordinates
def getGreeninfra(lng, lat):
	# lat = request.GET.get('lat','')
	# lng = request.GET.get('lng', '')
	# result = Greeninfra.objects.filter(latitude = lat, longitude = lng)

	# return HttpResponse(result.values())
	
#return averge greeninfra value from database using longitude, latitude
	values = []
	for obj in Greeninfra.objects.all():
		if (abs(lng - obj.lng) < 0.1 and abs(lat - obj.lng) < 0.1): # area threshold (0.1) for consideration
			values.append(obj.area)
	avg = avg(values)
	return avg

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