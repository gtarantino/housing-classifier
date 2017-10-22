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

      self.lmodel = linear_model.LinearRegression()
      self.lmodel.fit(ind_vars, target)

   # If the model contains the location then the model is applicable to the
   # record in which a user wants to make a prediction for.
   def is_applicable(self, location):
      return location in self.location_map

   def predict(self, record):
      loc = self.location_map[record['Location']]
      status = self.status_map[record['Status']]

      df = pd.DataFrame([[loc, status, record['Bedrooms'],
         record['Bathrooms'], record['Size']]],
         columns=['Location', 'Status', 'Bedrooms', 'Bathrooms', 'Size'])

      return self.lmodel.predict(df)
