import requests

class wUnderground():

	def __init__(self, key):
		self.key = key

	def weather(self, area):
		#apikey = "897522adf011af15"
		areaQuery = requests.get("http://autocomplete.wunderground.com/aq?query=%s" % area).json()

		searchData = areaQuery['RESULTS'][0]['l'] #Returns the first result

		jsonData = requests.get("http://api.wunderground.com/api/%s/conditions%s.json" % (self.key , searchData)).json()

		return jsonData