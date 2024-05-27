from tensorflow.keras.layers import Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.layers import LSTM,Bidirectional
from tensorflow.keras.layers import Dense,Dropout
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
corpus = []
from keras import models
from keras.models import load_model
import numpy as np

voc_size = 5000

model=load_model("bilstm.h5")
def predict(text):
    corpus = []
    review = re.sub('[^a-zA-Z]', ' ', text)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)
    print(corpus)
    one_hot_lbls = [one_hot(words,voc_size)for words in corpus]
    print(one_hot_lbls)
    Embedded_len = pad_sequences(one_hot_lbls,padding='pre',maxlen=20)
    print(Embedded_len)
    pr= model.predict(Embedded_len)
    pr1=np.round(pr)
    print(pr1)   
    #print(classes_x)



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from mlxtend.plotting import plot_confusion_matrix
from sklearn.metrics import confusion_matrix
data = pd.read_csv("./dataset/train.csv")

print(data.head())
print(data.shape)
print(data.isnull().sum())
data = data.dropna()

sns.set_style('darkgrid')
plt.figure(figsize=(10,8))
sns.countplot(x='label',data=data)


X = data.drop('label',axis=1)
y = data.label
print(X.shape,y.shape)


from tensorflow.keras.layers import Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.layers import LSTM,Bidirectional
from tensorflow.keras.layers import Dense,Dropout


voc_size = 5000

messages = X.copy()
#Text_input = messages.text[97]
Text_input = "There is a minefield of potential 2020 election candidates in the Democratic Party waiting to challenge President Trump, but most voters have not heard of many of them, according to a new poll. [The   Consult poll asked 1, 990 registered voters their views on 19 potential Democratic challengers to Trump s presidency.  The list of potential candidates identified in the survey includes eight senators, five governors, a mayor of a large city, a congressman, two CEOs, a former vice president, and a failed Senate candidate. Of those mentioned in the survey, half of the respondents did not know most of the candidates. All bets are off when it comes to the composition of the 2020 Democratic primary, said Morning Consult   and Chief Research Officer Kyle Dropp. This early polling indicates that many of the names being floated in Washington still have a lot of work to do in terms of building national profiles.  Most survey respondents were able to identify and have opinions on former Vice President Joe Biden, Sen. Elizabeth Warren, ( ) and Sen. Bernie Sanders ( ).   of the voters surveyed said they knew enough about Biden and Warren to have formed opinions about the candidates. Sanders was not included in the survey. According to Morning Consult, Biden was the most popular candidate of the list of potential 2020 Democratic candidates, with 74 percent of respondents having a positive view of the former vice president. Warren came in second, with 51 percent of respondents viewing her favorably. The number of those rumored to be potential Democratic candidates for the 2020 election pales in comparison to the list of people who have filed to run for president so   129 people have filed to run for the presidency in 2020."
        
print(type(Text_input))

predict(Text_input)
