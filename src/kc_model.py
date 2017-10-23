# Description: Kings County (Seattle area) linear regression model to predict
#              the price of a unit given a number of features.
#
# Model ID: 'KINGS_COUNTY'
# Model Features
# 'bedrooms'    - number of bedrooms
# 'bathrooms'   - number of bathrooms
# 'sqft_living' - square footage of the living space
# 'sqft_lot'    - square footage of the entire lot
# 'zipcode'     - zipcode the property is located in
# 'grade'       - overally grade given to the unit based on King County system
# 'condition'   - how good the overall condition of the house is
# 'yr_built'    - year in which the house was built

import pandas as pd
from sklearn import linear_model

class KingsCountyModel:
   def __init__(self):
      self.instantiate_model()

   def instantiate_model(self):
      self.df = pd.read_csv('../datasets/kc_house_data.csv')

      ind_vars = self.df[['bedrooms', 'bathrooms', 'sqft_living',
         'sqft_lot', 'zipcode', 'grade', 'condition', 'yr_built']]
      target = self.df['price']

      # Split the data into training and testing sets
      x = int(len(ind_vars) * 0.70)
      train_ind_vars = ind_vars[0:x]
      train_target = target[0:x]

      test_ind_vars = ind_vars[x:len(ind_vars)]
      test_target = target[x:len(target)]

      self.lmodel = linear_model.LinearRegression()
      self.lmodel.fit(train_ind_vars, train_target)
      print("Kings County Model R^2 Score:",
         self.lmodel.score(test_ind_vars, test_target))

   def predict(self, record):
      df = pd.DataFrame([[record['bedrooms'],
         record['bathrooms'], record['sqft_living'], record['sqft_lot'],
         record['zipcode'], record['grade'],
         record['condition'], record['yr_built']]],
         columns=['bedrooms', 'bathrooms', 'sqft_living',
         'sqft_lot', 'zipcode', 'grade', 'condition', 'yr_built'])

      return self.lmodel.predict(df)

def test():
   model = KingsCountyModel()

   test = {'model': 'KINGS_COUNTY', 'bedrooms': 3, 'bathrooms': 1,
      'sqft_living': 1180, 'sqft_lot': 5650, 'zipcode': 98178, 'grade': 7,
      'condition': 3, 'yr_built': 1955
   }

   print(model.predict(test))

if __name__ == '__main__':
   test()
