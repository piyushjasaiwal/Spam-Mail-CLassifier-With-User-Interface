from xml.sax.handler import all_features
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

import numpy as np
import pandas as pd

class classification:

    def __init__(self):
        self.data = pd.read_csv('./spam.csv')
        self.data.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis = 1, inplace = True)

        self.vectorizer = CountVectorizer(stop_words = 'english')

        self.data['category'] = self.data.v1.map({"spam":1, "ham":0})
        self.data['content'] = self.data.v2
        self.data.drop(['v1'], axis=1, inplace=True)
        self.data.drop(['v2'], axis=1, inplace=True)
        # print(self.data)

        all_features = self.vectorizer.fit_transform(self.data.content)

        X_train, X_test, y_train, y_test = train_test_split(all_features, self.data.category, test_size=0.3)

        self.classifier = MultinomialNB()

        self.classifier.fit(X_train, y_train)
        # print(len(y_test))
        # print((y_test == self.classifier.predict(X_test)).sum())

    def predict(self, string):
        string = [string]
        # string = pd.DataFrame(string)
        # string = string.reindex(labels = self.data.columns, axis=1)
        # features = self.vectorizer.fit_transform(string)
        features = self.vectorizer.transform(string)
        prediction = self.classifier.predict(features)
        return "Spam" if prediction == 1 else "Legitimate"

# c1 = classification()
# print(c1.predict("hello friend"))