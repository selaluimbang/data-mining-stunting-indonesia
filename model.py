import pickle

class StuntingModel:
    def __init__(self):
        self.model = None

    def load_model(self, path):
        best_model = pickle.load(open(path, 'rb'))
        self.model = best_model['model']

    def predict(self, features):
        return self.model.predict(features)
    
    def print_model(self):
        return(self.model)

    def print_features(self):
        columns = self.model.feature_names_in_
        return(columns)