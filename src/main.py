#!/usr/local/bin/python3

import pandas as pd
import numpy as np
from sklearn import linear_model

def predict_record(record):
   data_frame = pd.read_csv('../datasets/RealEstate.csv')

   ind_vars = pd.concat([
      data_frame['Location'].astype('category').cat.codes.rename('Location'),
      data_frame['Status'].astype('category').cat.codes.rename('Status'),
      data_frame[['Bedrooms', 'Bathrooms', 'Size']]],
      axis=1)
   target = data_frame['Price']

   lmodel = linear_model.LinearRegression()
   lmodel.fit(ind_vars, target)

   print('SCORE:', lmodel.score(ind_vars, target))
   print(lmodel.predict(record))

if __name__ == '__main__':
   test = pd.DataFrame([[0, 1, 3, 2, 1975]],
      columns=['Location', 'Status', 'Bedrooms', 'Bathrooms', 'Size'])
   predict_record(test)
