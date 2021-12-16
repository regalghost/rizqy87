import pandas as pd
import json
import matplotlib.pyplot as plt
import streamlit as st

#Streamlit Interface

st.subheader("N negara dengan Produksi Terbesar")





file_json = open('kode_negara_lengkap.json')
data_json = json.load(file_json)
excell = pd.read_csv('produksi_minyak_mentah.csv')
data_excel = pd.DataFrame(excell)


banyaknegara = st.slider(label = "Banyak Negara", min_value = 1, max_value= 142)

tahun = st.slider(label = "Tahun Produksi", min_value = 1970, max_value= 2015)
negara = []
produksi_terbanyak = data_excel[data_excel.tahun == tahun].produksi.sort_values(ascending = False)[:banyaknegara].values

for tiap_produksi in produksi_terbanyak:
    negara_produksi_terbanyak = data_excel[(data_excel.tahun == tahun) & (data_excel.produksi == tiap_produksi)].kode_negara.item()
    negara.append(negara_produksi_terbanyak)

x = negara
y = produksi_terbanyak

plt.plot(x, y)

