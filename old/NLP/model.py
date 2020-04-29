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

# data = pd.read_csv('text_emotion.csv')
# data = data.drop('author', axis=1)

data = pd.read_csv('text_emotion.csv')



# data = data.drop(data[data.sentiment == 'anger'].index)
# data = data.drop(data[data.sentiment == 'boredom'].index)
# data = data.drop(data[data.sentiment == 'enthusiasm'].index)
# data = data.drop(data[data.sentiment == 'empty'].index)
# data = data.drop(data[data.sentiment == 'fun'].index)
# data = data.drop(data[data.sentiment == 'relief'].index)
# data = data.drop(data[data.sentiment == 'surprise'].index)
# data = data.drop(data[data.sentiment == 'love'].index)
# data = data.drop(data[data.sentiment == 'hate'].index)
# data = data.drop(data[data.sentiment == 'worry'].index)


# data['content'] = data['content'].apply(lambda x: " ".join(x.lower() for x in x.split()))
# data['content'] = data['content'].str.replace('[^\w\s]',' ')

# nltk.download('stopwords')
# stop = stopwords.words('english')
# data['content'] = data['content'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))

# nltk.download('wordnet')
# data['content'] = data['content'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))

# def de_repeat(text):
#     pattern = re.compile(r"(.)\1{2,}")
#     return pattern.sub(r"\1\1", text)
# #%%
# data['content'] = data['content'].apply(lambda x: " ".join(de_repeat(x) for x in x.split()))

# freq = pd.Series(' '.join(data['content']).split()).value_counts()[-19000:]

# freq = list(freq.index)
# data['content'] = data['content'].apply(lambda x: " ".join(x for x in x.split() if x not in freq))

# lbl_enc = preprocessing.LabelEncoder()
# y = lbl_enc.fit_transform(data.sentiment.values)

# X_train, X_val, y_train, y_val = train_test_split(data.content.values, y, stratify=y, random_state=42, test_size=0.1, shuffle=True)

count_vect = CountVectorizer(analyzer='word')
count_vect.fit(data['content'])
# X_train_count =  count_vect.transform(X_train)
# X_val_count =  count_vect.transform(X_val)



# # Model 3: Logistic Regression
# logreg = LogisticRegression(C=1)
# logreg.fit(X_train_count, y_train)
# y_pred = logreg.predict(X_val_count)
# print('log reg count vectors accuracy %s' % accuracy_score(y_pred, y_val))



# filename = 'finalized_model.sav'
# pickle.dump(logreg, open(filename, 'wb'))


filename = 'finalized_model.sav'

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

