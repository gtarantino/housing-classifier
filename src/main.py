#!/usr/local/bin/python3

import pandas as pd
import numpy as np
from sklearn import linear_model

class HousingModel:
   def __init__(self):
      self.instantiate_model()

   def instantiate_model(self):
      self.df = pd.read_csv('../datasets/RealEstate.csv')

      ind_vars = pd.concat([
         self.df['Location'].astype('category').cat.codes.rename('Location'),
         self.df['Status'].astype('category').cat.codes.rename('Status'),
         self.df[['Bedrooms', 'Bathrooms', 'Size']]],
         axis=1)
      target = self.df['Price']

      self.lmodel = linear_model.LinearRegression()
      self.lmodel.fit(ind_vars, target)

      print('SCORE:', self.lmodel.score(ind_vars, target))

   def predict(self, record):
      print(self.lmodel.predict(record))

if __name__ == '__main__':
   model = HousingModel()
   test = pd.DataFrame([[0, 1, 3, 2, 1975]],
      columns=['Location', 'Status', 'Bedrooms', 'Bathrooms', 'Size'])
   model.predict(test)
