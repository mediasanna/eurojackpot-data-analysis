import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Lähteeksi käytän avointa suomendataa sivulta: https://www.avoindata.fi/data/fi/dataset/eurojackpotin-miljoonavoitot-historian-saatossa

df = pd.read_csv("eurojackpot.csv", encoding="cp1252")  # df = dataframe. Tuon encoding="cp1252" sain chatgpt:ltä apuna, kun en saanut streamlittiä toimimaan
# Seuraavat kolme riviä poistaa tekstit numeroriveiltä, koska ne näkyi häiritsevästi esim kaaviossa
df["Vuosi"] = pd.to_numeric(df["Vuosi"], errors="coerce")
df = df.dropna(subset=["Vuosi"])
df["Vuosi"] = df["Vuosi"].astype(int)

st.title("Eurojackpotin miljoonavoitot – yksinkertainen analyysi") # sain nämä kaksi otsikkoa myös chat:ltä, ja minusta nämä toimii kivasti ja saa datan paremmin visualisoitua
st.caption("Data: avoindata.fi – Eurojackpotin miljoonavoitot historian saatossa")

vuosittain = df.groupby("Vuosi")["Miljoonavoitot kierroksella"].sum().reset_index()

fig, ax = plt.subplots()
ax.bar(vuosittain["Vuosi"], vuosittain["Miljoonavoitot kierroksella"], color="skyblue")

ax.set_xlabel("Vuosi")
ax.set_ylabel("Miljoonavoittojen määrä")

# Tästä alespäin on vain perustietoja tästä datasta
st.write("Vuosittaiset miljoonavoitot (summa per vuosi):")
st.dataframe(vuosittain)

st.write("Datan koko")
st.write(df.size)

st.write("Sarakkeet ja niiden lukumäärä")
st.write(df.columns)
st.write("Sarakkeiden lukumäärä:", len(df.columns))

st.write("Aksikset – df.axes")
st.write(df.axes)

st.write("Datatyypit – df.dtype")
st.write(df.dtypes)

st.write("Datan muoto (rivit, sarakkeet) – df.shape")
st.write(df.shape)
