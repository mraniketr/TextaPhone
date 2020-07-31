import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
import pickle



filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

def extract_features(word_list):
  return dict([(word, True) for word in word_list])

input_reviews = [
    "Started off as the greatest series of all time, but had the worst ending of all time.",
    "Exquisite. 'Big Little Lies' takes us to an incredible journey with its emotional and intriguing storyline.",
    "I love Brooklyn 99 so much. It has the best crew ever!!",
    "The Big Bang Theory and to me it's one of the best written sitcoms currently on network TV.",
    "'Friends' is simply the best series ever aired. The acting is amazing.",
    "SUITS is smart, sassy, clever, sophisticated, timely and immensely entertaining!",
    "Cumberbatch is a fantastic choice for Sherlock Holmes-he is physically right (he fits the traditional reading of the character) and he is a damn good actor",
    "What sounds like a typical agent hunting serial killer, surprises with great characters, surprising turning points and amazing cast."
    "This is one of the most magical things I have ever had the fortune of viewing.",
    "I don't recommend watching this at all!"
]

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

