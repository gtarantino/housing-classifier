from global_model import GlobalModel

if __name__ == '__main__':
   model = GlobalModel()

   test = {'model': 'SLO_COUNTY', 'location': 'San Luis Obispo',
      'status': 'Foreclosure', 'bedrooms': 3, 'bathrooms': 2, 'size': 1104}
   model.predict(test)
