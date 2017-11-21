import json
import codecs
from datetime import date
from flask import Blueprint, request
from global_model import GlobalModel

content_api = Blueprint('content_api', __name__)

@content_api.route("/gethousingestimate", methods=['POST'])
def gethousingestimate():
   if request.method == 'POST':
      model = GlobalModel()

      # Get the payload body from the POST request
      #print(request.form)
      body = request.form

      if use_slo_model(request.form['location']):
         status = body['status'] if body['status'] != '' else 'Regular'
         bedrooms = int(body['bedrooms']) if body['bedrooms'] != '' else 2
         bathrooms = float(body['bathrooms']) if body['bathrooms'] != '' else 2
         size = int(body['sqft_living']) if body['sqft_living'] != '' else 1500

         record = {'model': 'SLO_COUNTY', 'location': body['location'],
            'status': status, 'bedrooms': bedrooms,
            'bathrooms': bathrooms, 'size': size}
      else:
         bedrooms = int(body['bedrooms']) if body['bedrooms'] != '' else 2
         bathrooms = float(body['bathrooms']) if body['bathrooms'] != '' else 2
         sqft_living = (int(body['sqft_living'])
            if body['sqft_living'] != '' else 1500)
         sqft_lot = int(body['sqft_lot']) if body['sqft_lot'] != '' else 7500
         zipcode = body['zipcode'] if body['zipcode'] != '' else "98003"
         grade = int(body['grade']) if body['grade'] != '' else 6
         condition = int(body['condition']) if body['condition'] != '' else 3
         yr_built = (int(body['year_built'])
            if body['year_built'] != '' else 1965)

         record = {'model': 'KINGS_COUNTY', 'bedrooms': bedrooms,
            'bathrooms': bathrooms, 'sqft_living': sqft_living,
            'sqft_lot': sqft_lot, 'zipcode': zipcode, 'grade': grade,
            'condition': condition, 'yr_built': yr_built}

      estimate = model.predict(record)

      return json.dumps({'estimate': estimate}), 200
   else:
      return 'No information for the given features', 500


def use_slo_model(city):
   cities = ['Arroyo Grande', 'Paso Robles', 'Morro Bay', 'Santa Maria-Orcutt',
       'Oceano', 'Atascadero', 'Los Alamos', 'San Miguel', 'San Luis Obispo',
       'Cayucos', 'Pismo Beach', 'Nipomo', 'Guadalupe', 'Los Osos', 'Templeton',
       'Grover Beach', 'Cambria', 'Solvang', 'Bradley', 'Avila Beach',
       'Santa Ynez', 'King City', 'Creston', 'Lompoc', 'Coalinga', 'Buellton',
       'Lockwood', 'Greenfield', 'Soledad', 'Santa Margarita', 'Bakersfield',
       'New Cuyama', 'San Simeon', 'Out Of Area']

   if city in cities:
      return True
   else:
      return False
