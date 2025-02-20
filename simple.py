import pickle

with open('artifacts/model_trainer/model.pkl', 'rb') as file:  # Open the file in read-binary mode
    data = pickle.load(file)  # Load the file content
    print(data)  # Display the object
