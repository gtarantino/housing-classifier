from slo_model import SloModel

class GlobalModel:
   def __init__(self):
      self.instantiate_models()

   # Add all models to the global model list
   def instantiate_models(self):
      self.models = []

      self.models.append(SloModel())

   # Find a model that can handle the given location
   def locate_model(self, location):
      for model in self.models:
         if model.is_applicable(location):
            return model

      return None

   # TODO allow this to accept record(s), need location to also have a state
   # or some more identifying features to correctly locate the appropriate model
   def predict(self, record):
      model = self.locate_model(record['Location'])

      if not model:
         print("No applicable model found")
         return

      print(model.predict(record))
