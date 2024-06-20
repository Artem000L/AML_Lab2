import pandas as pd
from sklearn.metrics import accuracy_score
import pickle

X_test = pd.read_csv('data/X_test.csv')
y_test = pd.read_csv('data/y_test.csv')

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f'Accuracy: {accuracy}')