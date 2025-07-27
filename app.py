import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la app
st.title("Análisis de Anuncios de Vehículos en EE.UU.")

# Cargar los datos
df = pd.read_csv("vehicles_us.csv")

# Mostrar los primeros registros
st.subheader("Vista general del dataset")
st.dataframe(df.head())

# Histograma del odómetro
st.subheader("Distribución del Odómetro")
nbins = st.slider("Número de bins", min_value=10, max_value=100, value=30)
fig1 = px.histogram(df, x='odometer', nbins=nbins, title='Distribución del odómetro')
st.plotly_chart(fig1)

# Gráfico de dispersión odómetro vs precio
st.subheader("Precio vs Odómetro por Condición")
fig2 = px.scatter(df, x='odometer', y='price', color='condition', title='Precio vs Odómetro')
st.plotly_chart(fig2)
