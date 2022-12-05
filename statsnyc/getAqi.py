def getAqi():

	from pandas import read_json

	url = 'https://api.waqi.info'

	# key: https://aqicn.org/data-platform/token/#/
	key = 'beb6375fb5bd62536b87aba304f09b629442758d'

	# bounds around New York via bboxfinder.com
	bounds = '40.541982,-74.047852,40.951900,-73.574066'

	urlBounds = f'/map/bounds/?latlng={bounds}&token={key}'
	data = read_json(url + urlBounds)


	for obj in data['data']:
		if obj['station']['name'] == 'New York':
			return int(obj['aqi'])




