import pandas as pd
import numpy as np
import pickle
import nltk
from nltk.corpus import stopwords
from textblob import Word
import re
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

filename = 'finalized_model.sav'
data = pd.read_csv('text_emotion.csv')

tweets = pd.DataFrame(['I am very happy today! The atmosphere looks cheerful',
'Things are looking great. It was such a good day',
'Success is right around the corner. Lets celebrate this victory',
'Martha was angry, certainly at the perpetrator but also at the Warwick police for not summarily arresting the man and rescuing the boy.',
'Now this is my worst, okay? But I am gonna get better.',
'I am tired, boss. Tired of being on the road, lonely as a sparrow in the rain. I am tired of all the pain I feel',
'This is quite depressing. I am filled with sorrow',
'His death broke my heart. It was a sad day'])
# Doing some preprocessing on these tweets as done before
tweets[0] = tweets[0].str.replace('[^\w\s]',' ')
from nltk.corpus import stopwords
stop = stopwords.words('english')
tweets[0] = tweets[0].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
from textblob import Word
tweets[0] = tweets[0].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))

#  Extracting Count Vectors feature from our tweets
# count_vect = CountVectorizer(analyzer='word')
# count_vect.fit(data['content'])

tweet_count = count_vect.transform(tweets[0])



loaded_model = pickle.load(open(filename, 'rb'))
tweet_pred = loaded_model.predict(tweet_count)


print(tweet_pred)
for i in range(0,len(tweet_pred)):
  if tweet_pred[i]==0:
    print("Happy")
  elif tweet_pred[i]==1:
    print("Neutral")
  else:
    print("Sad")

