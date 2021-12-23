from flask import Flask, render_template, request, jsonify
import requests

#Initializing app for Flask backend
app = Flask(__name__)
tomorrow_url = 'https://api.tomorrow.io/v4/timelines'

#Route for Homepage
@app.route('/')
def home():
   return app.send_static_file('homepage.html')

#Route to get Current,Daily,Hourly Weather Data from tomorrow.io API 
@app.route('/json-data')
def check_func():
   longitude = str(request.args['longitude'])
   latitude = str(request.args['latitude'])
   location = request.args['location']
   lat_lng = "zero"

   if location == "undefined" or (latitude != "0" and longitude != "0"):
      lat_lng = str(latitude)+","+str(longitude)
   else:
      lat_lng = str(location)

   #Setting Parameters to tomorrow.io API call
   API_PARAMS = {
      'apikey' : 'pHFfJMuGnh4uGIKWPqMhvIDsUFdkQT5x',
      'timesteps' : ['current','1d','1h'],
      'location':lat_lng,
      'units' : 'imperial',
      'fields' :  ['temperature', 'temperatureApparent', 'temperatureMin', 'temperatureMax','windSpeed','windDirection', 'humidity','pressureSeaLevel','uvIndex', 'weatherCode','precipitationProbability','precipitationType', 'sunriseTime', 'sunsetTime',
      'visibility','moonPhase',  'cloudCover']
   }

   response = requests.get(tomorrow_url, API_PARAMS)
   data = response.json()
   return jsonify(data)


if __name__ == '__main__':
   app.run()

