import pickle

pickle_file = open("C:\\Projects\\capstone-project\\trained_emotion_model.pkl", "rb")
pickle_data =pickle.load(pickle_file)
print(pickle_data)

