import streamlit as st
import pickle
import pandas as pd
import requests

st.title('MOVIE RECOMENDATION')
dict = pickle.load(open('MOVIE_RECOMENDATION.pkl','rb'))
df = pd.DataFrame(dict)

similarity_matix = pickle.load(open('MOVIE_RECOMENDATION_model_.pkl','rb'))



def recomend(movie):
  index = df[df['title'] == movie].index[0]
  recommeded_list = sorted(enumerate(similarity_matix[index]),reverse =True,key = lambda x : x[1])[1:4]
  recomm = []
  for i in recommeded_list:
    recomm.append(df.iloc[i[0]].title)
  return recomm

movieselected = st.selectbox("MOVIES:",df['title'].values)

if(st.button('RECOMMEND')):
    recommendations = recomend(movieselected)
    for i in recommendations:
        st.write(i)
# st.write("You selected:",selectbox)
# name = st.text_input("Enter your name")
# st.write(name)