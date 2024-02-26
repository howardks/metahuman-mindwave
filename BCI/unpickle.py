import pickle

pickle_file = open ("BCI\\Models\\AdaBoostClassifier_model.pkl", "rb")
pickle_data = pickle.load(pickle_file)
print(pickle_data)