from naive_bayes_scratch_oge import naive_bayes_predict, logprior, loglikelihood 
import pandas as pd

test_data = pd.read_csv("data_analysis2.csv")
data = test_data["content"].values.tolist()
scores=[]
for i in data:
    score = naive_bayes_predict(i, logprior,  loglikelihood)
    scores.append(score)
test_data["sentiment140_data_scores"] = scores
test_data.to_csv("data_analysis3.csv")
