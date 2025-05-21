import streamlit as st
import pandas as pd

st.set_page_config(page_title="CAGED", layout="wide")

try:
    df = pd.read_csv("streamlit/data.csv", sep=";")
    st.success("CSV carregado com sucesso")

    df['saldomovimentacao'] = df['saldomovimentacao'].replace({-1: 'desligado', 1: 'admitido'}, regex=True)
    df['sexo'] = df['sexo'].replace({1: 'masculino', 3: 'feminino'})

    st.dataframe(df)

except Exception as e:
    st.error(f"Erro ao carregar o CSV: {e}")
