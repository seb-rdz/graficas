# Para correr: streamlit run hola.py

# Importamos la librería Streamlit
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Crear el título para la aplicación web
st.title("Titanic App")
st.header("Titanic Graphs - App")
st.write("A01709461")

titanic_link = 'titanic(1).csv'
titanic_data = pd.read_csv(titanic_link)
st.dataframe(titanic_data)

fig, ax = plt.subplots() 
ax.hist(titanic_data.Fare) 
st.header("Histograma del Titanic") 
st.pyplot(fig)