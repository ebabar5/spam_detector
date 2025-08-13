import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB   
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score


df =pd.read_csv("backend/spam_assassin.csv")

x=df['text']
y=df['target']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
vec=TfidfVectorizer(max_features=10000,stop_words='english')
X_train_vec=vec.fit_transform(x_train)
X_test_vec=vec.transform(x_test)
model=MultinomialNB()
model.fit(X_train_vec,y_train)
y_pred=model.predict(X_test_vec)
accuracy=accuracy_score(y_test,y_pred)
# print(accuracy)


