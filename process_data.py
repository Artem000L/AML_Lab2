import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('data/wine.csv')

df['color'] = df['color'].replace({'red': 0, 'white': 1})

X = df.drop(columns=['color'])
y = df['color']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train.to_csv('data/X_train.csv', index=False)
X_test.to_csv('data/X_test.csv', index=False)
y_train.to_csv('data/y_train.csv', index=False)
y_test.to_csv('data/y_test.csv', index=False)