from googlemaps import Client

key = 'AIzaSyAMdqWfahFW7unCFRzrXMU5My6bYLkHStQ'


def geocode(place):
	gClient = Client(key = key)
	
	lat_ne = None
	lng_ne = None
	lat_sw = None
	lng_sw = None
	for area in place.split(' - '):
		gcode = gClient.geocode(address = place, components = {'administrative_area': 'NYC','country': 'US'})
		try:
			if lat_ne:
				if gcode[0]['geometry']['bounds']['northeast']['lat'] > lat_ne:
					lat_ne = gcode[0]['geometry']['bounds']['northeast']['lat']
			else:
				lat_ne = gcode[0]['geometry']['bounds']['northeast']['lat']

			if lng_ne:
				if gcode[0]['geometry']['bounds']['northeast']['lng'] > lng_ne:
					lng_ne = gcode[0]['geometry']['bounds']['northeast']['lng']
			else:
				lng_ne = gcode[0]['geometry']['bounds']['northeast']['lng']

			if lat_sw:
				if gcode[0]['geometry']['bounds']['southwest']['lat'] > lat_sw:
					lat_sw = gcode[0]['geometry']['bounds']['southwest']['lat']
			else:
				lat_sw = gcode[0]['geometry']['bounds']['southwest']['lat']

			if lng_sw:
				if gcode[0]['geometry']['bounds']['southwest']['lng'] > lng_sw:
					lng_sw = gcode[0]['geometry']['bounds']['southwest']['lng']
			else:
				lng_sw = gcode[0]['geometry']['bounds']['southwest']['lng']

		except:
			continue


	return ((lat_ne, lng_ne),
		(lat_sw, lng_sw))