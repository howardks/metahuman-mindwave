import pickle

pickle_file = open ("BCI\\Models\\XGBClassifier_model.pkl", "rb")
pickle_data = pickle.load(pickle_file)
print("DATA: ")
print(pickle_data)