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
import os
from werkzeug.utils import secure_filename
basepath = os.path.dirname(__file__)
mdl = os.path.join(basepath, 'static\\model', secure_filename('bilstm.h5'))  
voc_size = 5000

model=load_model(mdl)
def predict(text):
    corpus = []
    review = re.sub('[^a-zA-Z]', ' ', text)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)
    one_hot_lbls = [one_hot(words,voc_size)for words in corpus]
    Embedded_len = pad_sequences(one_hot_lbls,padding='pre',maxlen=20)
    pr= model.predict(Embedded_len)
    pr1=np.round(pr)
    return(pr1)   