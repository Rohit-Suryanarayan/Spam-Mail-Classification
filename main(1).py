import pandas as pd
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import pos_tag, word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

data = pd.read_csv("spamdata.csv")
print(data.head(15))

lemmatizer = WordNetLemmatizer()
# removing stopwords 
stopwords = set(stopwords.words('english'))

def review_messages(msg):
    # converting messages to lowercase
    msg = msg.lower()
    return msg
# Processing text messages
data['text'] = data['text'].apply(review_messages)
# training vectorizer using TF-IDF 
vectorizer = TfidfVectorizer()
df = vectorizer.fit_transform(data['text'])
#we are using svm for classification inbuilt libarary of sklearn is allowed if we use svm
from sklearn import svm
classifier = svm.SVC()
#Split data into 80% training & 20% testing data sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df, data['label'], test_size = 0.20, random_state = 0)
#accuracy of our model
from sklearn.metrics import classification_report,confusion_matrix, accuracy_score
pred = classifier.predict(X_test)
print(classification_report(y_test ,pred ))
print('Confusion Matrix: \n', confusion_matrix(y_test,pred))
print()
print('Accuracy: ', accuracy_score(y_test,pred))
#function to test future mails
def classify_new_mail(msg):
    msg = vectorizer.transform([msg])
    prediction = classifier.predict(msg)
    if prediction[0] == 'ham':
  return 0
    return “+1”
import os
path = "/home/piyush316/Downloads/PRML_assignment3/PRML_assignment3/test"
import os
dir_ = os.getcwd()
cur_dir = os.getcwd()
print(cur_dir)
os.chdir(path)
for file in os.listdir(cur_dir):
    if file.endswith(".txt"):
        print(file)
        f = open(file, 'r')
        text = f.read()
        res = classify_new_mail(text)
        str_output += str(res) +"\n"
        print(res)
        continue
    else:
        pass
f = open("final_output","a")
f.write(str_output)
f.close()
