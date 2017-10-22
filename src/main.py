from global_model import GlobalModel

if __name__ == '__main__':
   model = GlobalModel()

   test = {'Location': 'San Luis Obispo', 'Status': 'Foreclosure',
      'Bedrooms': 3, 'Bathrooms': 2, 'Size': 1104}
   model.predict(test)
