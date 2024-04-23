# Para correr: streamlit run hola.py

# Importamos la librería Streamlit
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Crear el título para la aplicación web
st.title("Titanic App")
st.header("Titanic Graphs - App")
st.write("Sebastián Rodríguez | A01709461")

titanic_link = 'titanic(1).csv'
titanic_data = pd.read_csv(titanic_link)
st.dataframe(titanic_data)

# GRAFICA 1 
fig, ax = plt.subplots() 
ax.hist(titanic_data.Fare) 
st.header("Histograma del Titanic") 
st.pyplot(fig)

# GRAFICA 2
fig2, ax2 = plt.subplots()
y_pos = titanic_data['Pclass']
x_pos = titanic_data['Fare']
ax2.barh(y_pos, x_pos)
ax2.set_ylabel("Pclass")
ax2.set_xlabel("Fare")
ax2.set_title('¿Cuanto pagaron las clases del Titanic')
st.header("Grafica de Barras del Titanic")
st.pyplot(fig2)

# GRAFICA 3 
fig3, ax3 = plt.subplots()
ax3.scatter(titanic_data.Age, titanic_data.Fare)
ax3.set_xlabel("Edad")
ax3.set_ylabel("Tarifa")
st.header("Grafica de Dispersión del Titanic")
st.pyplot(fig3)

# GRAFICA 4 
fig4, ax4 = plt.subplots() 
ax4 = titanic_data.boxplot(['Age'])
ax4.set_ylabel('Edad')
st.header('Gráfica de cajas por Edad')
st.pyplot(fig4)

# GRAFICA 5 
fig5, ax5 = plt.subplots()
hist_class = np.histogram(titanic_data["Pclass"], bins=3, range=(1,3))[0]
labels = ['Clase 1', 'Clase 2', 'Clase 3']
colors = ['tab:blue', 'tab:red', 'tab:green']
explode = [0, 0, 0.2]
ax5.pie(hist_class,
       labels = labels,
         colors = colors,
         autopct='%.0f%%',
         explode = explode,
         shadow = True)
st.header("Grafica de pastel - Clase social")
st.pyplot(fig5)
st.dataframe(hist_class)