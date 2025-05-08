import streamlit as st
import pickle
import string
import nltk
#nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

#import os

#import nltk

#nltk.data.path.append('C:\\Users\\panse\\AppData\\Roaming\\nltk_data')
#nltk.download('stopwords')

#stopwords.words('english')


def transforming_text(t):
    t = t.lower()
    t = nltk.word_tokenize(t)
    
    z=[]
    for i in t:
        if i.isalnum():
            z.append(i)
            
    t = z[:]
    z.clear()
    
    for i in t:
        if i not in stopwords.words('english') and i not in string.punctuation:
            z.append(i)
            
    t = z[:]
    z.clear()
    
    for i in t:
        z.append(ps.stem(i))
        
            
    return " ".join(z)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Sms/Email Spam Predictor")

input_msg = st.text_area("Enter your message")

if st.button("Predict"):

    transformed_text = transforming_text(input_msg)

    vector_input = tfidf.transform([transformed_text])

    result = model.predict(vector_input)[0]

    if result ==1:
        st.header("Spam")
    else:
        st.header("Not Spam")
      








