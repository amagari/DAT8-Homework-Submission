import pandas as pd
import requests
import matplotlib as plt
## Reading in the data

url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/yelp.csv"
yelp = pd.read_csv(url)

## dataframe with only the entries with 1 and 5

fiveandonestars = yelp[(yelp.stars == 5) | (yelp.stars == 1)]

#creating the feature and response

X = fiveandonestars.text
y = fiveandonestars.stars

# Creating training and testing sets
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y)

## using CountVectorizer to create document term matrices

from sklearn.feature_extraction.text import CountVectorizer

vect = CountVectorizer()

## Learning the vocabulary of the text
X_train_dtm = vect.fit(X_train)
X_test_dtm = vect.fit(X_test)
#Creating a document-term matrix in the same variable
X_train_dtm = vect.transform(X_train)
X_test_dtm = vect.transform(X_test)

## After vectorizing the text of the documents, 
# Training the Naive Bayes model

from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(X_train_dtm, y_train)

#Making class predictions for test data
y_pred_class = nb.predict(X_test_dtm)

## testing the accuracy of the predictions from the test data
## against 

from sklearn import metrics

print metrics.accuracy_score(y_test,y_pred_class)

## This is a far as I was able to get


