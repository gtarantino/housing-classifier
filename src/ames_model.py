# Description: Ames city linear regression model to predict
#              the price of a unit given a number of features.
#
# Model ID: 'AMES_CITY'
# Model Features:

import pandas as pd
from sklearn import linear_model

class AmesModel:
   num_features = [
      'BedroomAbvGr',
      'FullBath',
      'HalfBath',
      'YearBuilt',
      'GrLivArea',
      'LotArea',
      'Fireplaces',
      'OverallCond'
   ]

   cat_features = [
      'CentralAir'
   ]

   def __init__(self):
      self.instantiate_model()

   def instantiate_model(self):
      df_train = pd.read_csv('../datasets/ames_train.csv')

      ind_vars = pd.concat([
         df_train[AmesModel.num_features],
         df_train['CentralAir'].astype('category').cat.codes.rename('CentralAir')
      ], axis=1)
      target = df_train['SalePrice']

      # Maps
      self.central_air_map = {v: k for k, v in
         dict(enumerate(df_train['CentralAir']
         .astype('category').cat.categories)).items()}

      # Split the data into training and testing sets
      x = int(len(ind_vars) * 0.70)
      train_ind_vars = ind_vars[0:x]
      train_target = target[0:x]

      test_ind_vars = ind_vars[x:len(ind_vars)]
      test_target = target[x:len(target)]

      self.lmodel = linear_model.LinearRegression()
      self.lmodel.fit(train_ind_vars, train_target)
      print("Ames Model R^2 Score:",
         self.lmodel.score(test_ind_vars, test_target))

   def predict(self, record):
      df = pd.DataFrame([[
         record['BedroomAbvGr'],
         record['FullBath'],
         record['HalfBath'],
         record['YearBuilt'],
         record['GrLivArea'],
         record['LotArea'],
         record['Fireplaces'],
         record['OverallCond'],
         self.central_air_map[record['CentralAir']]
         ]], columns=AmesModel.num_features + AmesModel.cat_features)

      return self.lmodel.predict(df)

def test():
   model = AmesModel()

   test = {
      'model': 'AMES_CITY',
      'BedroomAbvGr': 3,
      'FullBath': 2,
      'HalfBath': 1,
      'YearBuilt': 2003,
      'GrLivArea': 1710,
      'LotArea': 8450,
      'Fireplaces': 0,
      'OverallCond': 5,
      'CentralAir': 'Y'
   }

   print(model.predict(test))

if __name__ == '__main__':
   test()
