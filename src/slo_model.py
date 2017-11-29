# Description: San Luis Obispo county linear regression model to predict the
#              price of a unit given a number of features.
#
# Model ID: 'SLO_COUNTY'
# Model Features:
# 'location'  - city/town where the unit is located
# 'status'    - type of sale ('Short Sale', 'Foreclosure', 'Regular')
# 'bedrooms'  - number of bedrooms
# 'bathrooms' - number of bathrooms
# 'size'      - square footage of living space

import pandas as pd
from sklearn import linear_model

class SloModel:
   def __init__(self):
      self.instantiate_model()

   def instantiate_model(self):
      self.df = pd.read_csv('../datasets/slo_county_real_estate.csv')

      ind_vars = pd.concat([
         self.df['Location'].astype('category').cat.codes.rename('Location'),
         self.df['Status'].astype('category').cat.codes.rename('Status'),
         self.df[['Bedrooms', 'Bathrooms', 'Size']]],
         axis=1)
      target = self.df['Price']

      self.location_map = {v: k for k, v in
         dict(enumerate(self.df['Location']
         .astype('category').cat.categories)).items()}
      self.status_map = {v: k for k, v in
         dict(enumerate(self.df['Status']
         .astype('category').cat.categories)).items()}

      # Split the data into training and testing sets
      x = int(len(ind_vars) * 0.70)
      train_ind_vars = ind_vars[0:x]
      train_target = target[0:x]

      test_ind_vars = ind_vars[x:len(ind_vars)]
      test_target = target[x:len(target)]

      self.lmodel = linear_model.LinearRegression()
      self.lmodel.fit(train_ind_vars, train_target)
      print("SLO County Model R^2 Score:",
         self.lmodel.score(test_ind_vars, test_target))

   def predict(self, record):
      loc = self.location_map[record['location']]
      status = self.status_map[record['status']]

      df = pd.DataFrame([[loc, status, record['bedrooms'],
         record['bathrooms'], record['size']]],
         columns=['Location', 'Status', 'Bedrooms', 'Bathrooms', 'Size'])

      return self.lmodel.predict(df)

def test():
   model = SloModel()

   test = {'model': 'SLO_COUNTY', 'location': 'San Luis Obispo',
      'status': 'Foreclosure', 'bedrooms': 3, 'bathrooms': 2, 'size': 1104}
   print(model.predict(test))

if __name__ == '__main__':
   test()
