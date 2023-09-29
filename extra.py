import pandas as pd
df = pd.read_csv("sentiment140dataset.csv")
print(df.head())

pos_mask = df['sentiment'].isin([0])
p_data = df[pos_mask]
p_data.to_csv("positive_data.csv", index=False)

neg_mask = df['sentiment'].isin([4])
n_data = df[neg_mask]
n_data.to_csv("negative_data.csv")