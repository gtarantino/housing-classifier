from slo_model import SloModel
from kc_model import KingsCountyModel

class GlobalModel:
   def __init__(self):
      self.instantiate_models()

   # Add all models to the global model list
   def instantiate_models(self):
      self.models = {}

      self.models['SLO_COUNTY'] = SloModel()
      self.models['KINGS_COUNTY'] = KingsCountyModel()

   # Find a model that can handle the given location
   def locate_model(self, model_name):
      if model_name in self.models:
         return self.models[model_name]

      return None

   # TODO allow this to accept record(s), need location to also have a state
   # or some more identifying features to correctly locate the appropriate model
   def predict(self, record):
      model = self.locate_model(record['model'])

      if not model:
         print("No applicable model found")
         return

      estimate = model.predict(record)

      print(estimate)
      return estimate[0]
