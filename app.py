import streamlit as st
import pandas as pd
import requests
import pickle


with open('movie_data.pkl','rb') as file:
    movies,cosine_sim = pickle.load(file)


    def get_recommendations(title, cosine_sim=cosine_sim):
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
     
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11] #to get 10 similar movies
    movie_indices = [i[0] for i in sim_scores]
    return  movies['title'].iloc[movie_indices]