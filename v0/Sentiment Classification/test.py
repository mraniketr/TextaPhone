import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
import pickle



filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

def extract_features(word_list):
  return dict([(word, True) for word in word_list])

input_reviews = []
input_reviews.append(input("Enter Data"))

for review in input_reviews:
    print("\nReview:", review)
    probdist = loaded_model.prob_classify(extract_features(review.split()))
    pred_sentiment = probdist.max()

for review in input_reviews:
    print("\nReview:", review)
    probdist = loaded_model.prob_classify(extract_features(review.split()))
    pred_sentiment = probdist.max()
    print("Predicted sentiment: ", pred_sentiment)
    print("Probability: ", round(probdist.prob(pred_sentiment), 2))

