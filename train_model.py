import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

X_train = pd.read_csv('data/X_train.csv')
y_train = pd.read_csv('data/y_train.csv')

model = RandomForestClassifier()
model.fit(X_train, y_train.values.ravel())

with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)