# Import all libraries
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model

# Load the imdb dataset word index
word_index = imdb.get_word_index()
reverse_word_index = {value : key for key, value in word_index.items()}

# Load the pre-trained model with ReLu activation
model = load_model('simple_rnn_imdb.h5')

## Helper functions

## 1. Function to decode review
def decode_review(encoded_review):
    return ' '.joim([reverse_word_index.get(i-3, '?') for i in encoded_review])

## 2. Function to preprocess the user input
def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review

### Prediction function
def predict_sentiment(review):
    preprocessed_input = preprocess_text(review)

    prediction = model.predict(preprocessed_input)

    sentiment = 'Positive' if prediction[0][0] > 0.5 else 'Negative'

    return sentiment, prediction[0][0]


import streamlit as st
## Streamlit app
st.title('IMDB Movie Review Sentiment Analysis')
st.write('Enter a movie review to classify it as positive or negative:')

## User input
user_input = st.text_area('Movie Review')

show_example = st.checkbox("Show example")
if show_example:
    st.write(f"* *this movie was really good i liked the story and the acting was great.*")
    st.write(f"* *i did not like this film it was slow and the characters were weak.*")

if st.button('Classify'):
    sentiment, prediction = predict_sentiment(user_input)

    ## Display the result
    st.write(f'**Sentiment: {sentiment}**')
    st.write(f'**Prediction Score: {prediction}**')
else:
    st.write('Please enter a movie review.')