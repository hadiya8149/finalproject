import pickle
model_pkl_file = "naive_model"

with open(model_pkl_file, 'rb') as file:
    model = pickle.load(file)

    score = model.naive_bayes_predict("I am happy")
    print(score)