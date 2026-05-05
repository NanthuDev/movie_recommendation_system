import streamlit as st
import pandas as pd
import requests
import pickle


with open('movie_data.pkl','rb') as file:
    movies,cosine_sim = pickle.load(file)